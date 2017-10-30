import datetime

from app import db


class TimeStampedModelMixin:
    """
     An Mixin base class model that provides self-updating
    ``created_at`` and ``modified_at`` fields.
    """
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)


class User(db.Model, TimeStampedModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def as_dict(self):
        return {
            "id":  self.id,
            "username":  self.username,
            "email":  self.email,
        }

    def __repr__(self):
        return '<User %r>' % self.username


def create_schema():
    db.drop_all()
    db.create_all()
