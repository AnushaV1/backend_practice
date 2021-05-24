from app import app
from models import db, User


db.drop_all()
db.create_all()

u1 = User(
    firstname='Bridge',
    middlename='',
    lastname='Mike',
    email='testbridge@email.com',
    age=26,
    version_id=1
    
)

u2 = User(
    firstname='Allen',
    middlename='',
    lastname='Peter',
    email='allen@email.com',
    age=35,
    version_id=1
    
)

u3 = User(
    firstname='Bridge',
    middlename='',
    lastname='Mike',
    email='mike@email.com',
    age=30,
    version_id=1
    
)

db.session.add_all([u1, u2, u3])
db.session.commit()