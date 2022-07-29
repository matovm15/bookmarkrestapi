from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
db = SQLAlchemy()


# User Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, onupdate=datetime.now())
    Buckets = db.relationship('Bucket', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.username}'

# Bucket Database Model
class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # body = db.Column(db.Text, nullable=True)
    name = db.Column(db.Text, nullable=False)
    # short_url = db.Column(db.String(3), nullable=True)
    # visits = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_modified = db.Column(db.DateTime, onupdate=datetime.now())

    # def generate_short_characters(self):
    #     characters = string.digits+string.ascii_letters
    #     picked_chars = ''.join(random.choices(characters, k=3))

    #     link = self.query.filter_by(short_url=picked_chars).first()

    #     if link:
    #         self.generate_short_characters()
    #     else:
    #         return picked_chars

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     self.short_url = self.generate_short_characters()

    def __repr__(self) -> str:
        return 'Bucket >>> {self.url}'
