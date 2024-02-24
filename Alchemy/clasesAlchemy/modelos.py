#from sqlalchemy import Column, Integer, String
from clasesAlchemy import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    apPat = db.Column(db.String(200), nullable=False)
    apMat = db.Column(db.String(200))
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(500))
    profilePicture = db.Column(db.String(200))
    superUser = db.Column(db.Integer)

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    genero = db.Column(db.String(45))
    duracion = db.Column(db.Integer)
    inventario = db.Column(db.Integer, nullable=False, default=1)

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = db.Column(db.Integer, db.ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = db.Column(db.DateTime, nullable=False)
    dias_de_renta = db.Column(db.Integer, default=5)
    estatus = db.Column(db.Integer, default=0)