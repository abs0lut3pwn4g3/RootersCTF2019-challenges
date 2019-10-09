''' User views '''

from datetime import timedelta
from flask import request, jsonify, make_response, redirect, json, render_template
from flask_jwt_extended import (create_access_token, jwt_required)
from flask_restful import Resource
from flask_login import login_user, current_user
from sqlalchemy.exc import IntegrityError, InvalidRequestError

from src import db, api

from .models import User
from .schemas import UserSchema

class UserLoginResource(Resource):
    model = User
    schema = UserSchema

    def get(self):
        return make_response(render_template('login.html'))

    def post(self):

        if request.json:
            data = request.json
            user = self.model.query.filter(self.model.email == data['email']).first()
            if user and self.model.check_password(user, data['password']):
                expires = timedelta(days=365)
                user = UserSchema(only=('id', 'email', 'is_admin')).dump(user).data
                return make_response(
                    jsonify({'id': user,
                             'authentication_token': create_access_token(identity=user['id'], expires_delta=expires)}), 200)
            else:
                return make_response(jsonify({"error": {"code": 400, "msg": "No such user/wrong password."}}), 400)

        else:
            data = request.form
            user = self.model.query.filter(self.model.email == data['email']).first()
            if user and self.model.check_password(user, data['password']) and login_user(user):
                return make_response(redirect('/admin/', 302))
            else:
                return make_response(redirect('/api/v1/login', 403))


class UserRegisterResource(Resource):
    model = User
    schema = UserSchema

    def post(self):
        data = request.json
        if not data:
            return make_response(jsonify({'error': 'No data'}), 400)
        user = User.query.filter(User.email == data['email']).first()
        if user:
            return make_response(jsonify({'error': 'User already exists'}), 403)
        user, errors = self.schema().load(data)
        if errors:
            return make_response(jsonify(errors), 400)
        try:
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
        except (IntegrityError, InvalidRequestError) as e:
            print(e)
            db.session.rollback()
            return make_response(jsonify(error={'code': 400 }), 400)

        expires = timedelta(days=365)
        return make_response(
            jsonify(created_user={'id': user.id,
                        'user': self.schema(only=('id', 'email', 'is_admin')).dump(user).data,
                        'authentication_token': create_access_token(identity=user.id,
                                                                                expires_delta=expires)}), 200)

                                                                                
api.add_resource(UserLoginResource, '/login/', endpoint='login')
api.add_resource(UserRegisterResource, '/register/', endpoint='register')