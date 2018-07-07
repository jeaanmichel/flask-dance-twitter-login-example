from app import db
from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin


class User(UserMixin, db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(100), unique=True)


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
