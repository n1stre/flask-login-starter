from app import db
from app.helpers import ts

class Command(db.Model):
  id            = db.Column(db.Integer, primary_key=True)
  type          = db.Column(db.String(20))
  name          = db.Column(db.String(50))
  user_id       = db.Column(db.Integer, db.ForeignKey('user.id'))
  date_created  = ts.created(db)
  date_modified = ts.modified(db)

  def __init__(self, name):
    self.name = name

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return Command.query.all()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Command: {}>".format(self.name)