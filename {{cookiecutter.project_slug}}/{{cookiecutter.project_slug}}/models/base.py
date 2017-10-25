from app import db


class User(db.Model):
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
