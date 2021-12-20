import os
from datetime import datetime
from . import db


class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    #date_added = db.Column(db.DateTime(), default=datetime.utcnow)
    #date_joined = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return self.title
