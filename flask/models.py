from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', backref='grupo', lazy=True)

class Carrera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', backref='carrera', lazy=True)

class Universidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', backref='universidad', lazy=True)

class Profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', backref='profesor', lazy=True)

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), nullable=False)
    carrera_id = db.Column(db.Integer, db.ForeignKey('carrera.id'), nullable=False)
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'), nullable=False)
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.id'), nullable=False)