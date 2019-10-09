from flask_login import current_user, UserMixin
from src import db, ReprMixin, BaseMixin, bcrypt, login_manager
from src.notifs.models import Notification

''' User Table '''

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, ReprMixin, BaseMixin, UserMixin):
    __repr_fields__ = ['id', 'email', 'is_admin']

    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    notifications = db.relationship('Notification', back_populates='issuer', uselist=True)
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
