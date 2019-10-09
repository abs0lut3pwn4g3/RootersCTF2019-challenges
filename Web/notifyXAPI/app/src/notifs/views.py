from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Notification
from .schemas import notifications_schema, notification_schema
from src import db, api
from src.users.models import User
from flask_jwt_extended.exceptions import InvalidHeaderError, NoAuthorizationError, JWTExtendedException

class Notifications_api(Resource):

    @jwt_required
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            if user.is_admin:
                all_notifs = Notification.query.all()
            else:
                all_notifs = Notification.query.join(User).filter(User.is_admin == False).all()
            return jsonify(notifications_schema.dump(all_notifs).data)
        except (InvalidHeaderError, NoAuthorizationError, JWTExtendedException) as e:
            return make_response(jsonify({'meta': {'code': 404, 'error': str(e) }}), 404)

    @jwt_required
    def post(self):
        current_user_id = get_jwt_identity()

        title = request.json['title']
        body = request.json['body']
        issuer_id = current_user_id

        new_notif = Notification(title, body, issuer_id)

        db.session.add(new_notif)
        db.session.commit()

        return jsonify(notification_schema.dump(new_notif).data)

api.add_resource(Notifications_api, '/notifications/')