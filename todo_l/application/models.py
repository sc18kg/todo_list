from application import db
from datetime import datetime

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(30))
    done = db.Column(db.Boolean, default=False)
  ##  owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

##class Owners(db.Model):
   ## id = db.Column(db.Integer, primary_key=True)
   ## firstname = db.Column(db.String(30), nullable=False)
  ##  surname = db.Column(db.String(30), nullable=False)
  ##  tasks = db.relationship('Tasks', backref='owner')