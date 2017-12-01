from app import db
from app.helpers import ts_created, ts_modified

class Base(db.Model):
  __abstract__  = True

  id  = db.Column(db.Integer, primary_key=True)
  date_created  = ts_created(db)
  date_modified = ts_modified(db)

class Command(Base):
  type    = db.Column(db.String(50))
  name    = db.Column(db.String(50), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  @staticmethod
  def get_all():
    return Command.query.all()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Command: {}>".format(self.name)