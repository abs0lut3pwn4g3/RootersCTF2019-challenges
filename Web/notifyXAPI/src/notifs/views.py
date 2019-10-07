from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Notification
from .schemas import notifications_schema, notification_schema
from src import db, api

class Notifications_api(Resource):

    @jwt_required
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            all_notifs = Notification.query.filter(Notification.issuer_id == current_user_id).all()
            return jsonify(notifications_schema.dump(all_notifs).data)
        except Exception as e:
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