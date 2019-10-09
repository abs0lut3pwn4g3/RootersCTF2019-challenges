''' Models '''

from src import db
from datetime import datetime
from src.utils import BaseMixin, ReprMixin
# from src.users.models import User

''' Notifications Table '''

class Notification(BaseMixin, ReprMixin, db.Model):
    __repr_fields__ = [ 'title', 'body', 'issuer' ]

    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(250), nullable=False)
    issuer_id = db.Column(db.ForeignKey('user.id'), nullable=False)

    issuer = db.relationship('User', foreign_keys=[issuer_id], back_populates='notifications', lazy='subquery')

    def __init__(self, title, body, issuer_id):
      self.title = title
      self.body = body
      self.issuer_id = issuer_id

