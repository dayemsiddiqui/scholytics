from app import db
from models.auth import *

db.create_all()

# db.session.add(User("name","some@email.com", "mypass123"))

db.session.commit()
