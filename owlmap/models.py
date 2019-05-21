from datetime import datetime
from owlmap import db

class User(db.Model):
    exp = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.nombres}', '{self.apellidos}')"


class Edificio(db.Model):
    clave = db.Column(db.String(15), primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')

    def __repr__(self):
        return f"Edificios('{self.clave}', '{self.nom}' , ' {self.lat}' , '{self.lng}')"


class Cubiculo(db.Model):
    clave = db.Column(db.String(15), primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')
    edif = db.relationship('Edificios', backref='edificio', lazy=True)

    def __repr__(self):
        return f"Cubiculos('{self.clave}', '{self.nom}' , ' {self.lat}' , '{self.lng}')"


class Salon(db.Model):
    clave = db.Column(db.String(15), primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nom = db.Column(db.String(60), nullable=False)
    desc = db.Column(db.String(240), nullable=False, default='')
    edif = db.relationship('Edificios', backref='edificio', lazy=True)

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
    cubo = db.Column(db.String(15), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.Integer)

    def __repr__(self):
        return f"Maestro('{self.nombres}', '{self.apellidos}', '{self.email}')"
