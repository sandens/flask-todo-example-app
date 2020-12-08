from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Sequence, Integer

db=SQLAlchemy()

class Todo(db.Model):
       __tablename__ = 'todos'
       
       id = db.Column('todo_id', db.Integer, primary_key = True)
       name = db.Column(db.String(100))