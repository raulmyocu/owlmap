from datetime import datetime
from owlmap import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    exp = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.nombres}', '{self.apellidos}')"

    def get_id(self):
        return (self.exp)


class Edificio(db.Model):
    clave = db.Column(db.String(15), primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')
    cubiculos = db.relationship('Cubiculo', backref='edificio', lazy=True)
    salones = db.relationship('Salon', backref='edificio', lazy=True)

    def __repr__(self):
        return f"Edificios('{self.clave}', '{self.nom}' , ' {self.lat}' , '{self.lng}')"


class Cubiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clave = db.Column(db.String(15), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')
    edif_clave = db.Column(db.String(15), db.ForeignKey('edificio.clave'), nullable=False)
    maestro = db.relationship('Maestro', backref='cubiculo', lazy=True)

    def __repr__(self):
        return f"Cubiculos('{self.clave}', '{self.nom}' , ' {self.lat}' , '{self.lng}')"


class Salon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clave = db.Column(db.String(15), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')
    edif_clave = db.Column(db.String(15), db.ForeignKey('edificio.clave'), nullable=False)

    def __repr__(self):
        return f"Salones('{self.clave}', '{self.nom}' , ' {self.lat}' , '{self.lng}')"


class Servicios(db.Model):
    clave = db.Column(db.String(15), primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')

    def __repr__(self):
        return f"Servicios('{self.clave}', '{self.nom}' , ' {self.lat}' , '{self.lng}')"


class Maestro(db.Model):
    exp = db.Column(db.Integer, primary_key=True)
    cubo = db.Column(db.Integer, db.ForeignKey('cubiculo.id'), nullable=True)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.Integer)

    def __repr__(self):
        return f"Maestro('{self.nombres}', '{self.apellidos}', '{self.email}')"
