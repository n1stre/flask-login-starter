from app import db
from app.helpers import ts

class User(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'users'

    id            = db.Column(db.Integer, primary_key=True)
    public_id     = db.Column(db.String(50), unique=True)
    name          = db.Column(db.String(50))
    password      = db.Column(db.String(80))
    admin         = db.Column(db.Boolean)
    date_created  = ts.created(db)
    date_modified = ts.modified(db)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)