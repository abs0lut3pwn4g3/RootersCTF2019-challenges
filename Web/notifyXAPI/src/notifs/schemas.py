from src import ma, BaseSchema
from src.users.schemas import UserSchema
from .models import Notification

# Notification Schema
class NotificationSchema(BaseSchema):
	class Meta:
		model = Notification
		fields = ('id', 'issuer', 'title', 'body')

	id = ma.Integer(dump_only=True)
	title = ma.String(required=True)
	body = ma.String(required=True)
	issuer = ma.Nested(UserSchema, many=False, only=('id', 'email'))

notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many=True)