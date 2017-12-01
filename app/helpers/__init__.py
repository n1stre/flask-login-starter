def ts_created(db):
  return db.Column(
    db.DateTime, 
    default=db.func.current_timestamp()
  )

def ts_modified(db):
  return db.Column(
    db.DateTime, 
    default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp()
  )
