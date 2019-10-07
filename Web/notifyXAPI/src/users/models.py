from flask_login import current_user, UserMixin
from src import db, ReprMixin, bcrypt, login_manager

''' User Table '''

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, ReprMixin, UserMixin):
    __repr_fields__ = ['id', 'email', 'is_admin']

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
