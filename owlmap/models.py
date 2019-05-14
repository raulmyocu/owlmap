from datetime import datetime
from owlmap import db

class User(db.Model):
    exp = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.nombres}', '{self.apellidos}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_exp = db.Column(db.Integer, db.ForeignKey('user.exp'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Point(db.Model):
    clave = db.Column(db.String(15), primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')

    def __repr__(self):
        return f"Point('{self.nom}', '{self.lat}', '{self.lng}')"

class Maestro(db.Model):
    exp = db.Column(db.Integer, primary_key=True)
    cubo = db.Column(db.String(15), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.Integer)

    def __repr__(self):
        return f"Maestro('{self.nombres}', '{self.apellidos}', '{self.email}')"
