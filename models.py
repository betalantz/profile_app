from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Profile(db.Model, SerializerMixin):
    __tablename__ = 'birds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    address = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return f'<Profile {self.name} | username: {self.username}>'