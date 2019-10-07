''' Models '''

from src import db
from datetime import datetime
from src.users.models import User
from src.utils import ReprMixin

''' Notifications Table '''

class Notification(ReprMixin, db.Model):
    __repr_fields__ = [ 'title', 'body', 'issuer' ]

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(250), nullable=False)
    issuer_id = db.Column(db.ForeignKey('user.id'), nullable=False)

    issuer = db.relationship('User', uselist=False, foreign_keys=[issuer_id], backref='my_notifications', lazy='subquery')

    def __init__(self, title, body, issuer_id):
      self.title = title
      self.body = body
      self.issuer_id = issuer_id

