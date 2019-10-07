from .models import User
from src import ma, BaseSchema

# User Schema
class UserSchema(BaseSchema):
    class Meta:
        model = User

    id = ma.Integer(dump_only=True)
    is_admin = ma.Boolean(dump_only=True)
    email = ma.Email(required=False)