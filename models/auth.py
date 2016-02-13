import sys
sys.path.append('...')
from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(255), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    profile = db.relationship('Profile', backref='user',cascade="all,delete", uselist=False)
    verified = db.Column(db.Boolean)

    def __init__(self, username, email, password, profile):
        self.username = username
        self.email = email
        self.password = password
        self.profile = profile
        self.verified = False

    def __repr__(self):
        return '<User %r>' % self.username


# ================================
#          Profile Table
# ================================

class Profile(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name =  db.Column(db.String(80), nullable = False)
        date_of_birth = db.Column(db.String(80), nullable = False)
        institute = db.Column(db.Text, nullable = False)
        profession = db.Column(db.String(50), nullable = False)
        education = db.Column(db.String(50), nullable = False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

        def __init__(self, name="", date_of_birth="", institute="", profession="", education=""):
            self.name = name
            self.date_of_birth = date_of_birth
            self.institute = institute
            self.profession = profession
            self.education = education

        def __repr__(self):
            return '<Name %r>' % self.name
