from app import app, db
from models import Grupo, Carrera, Universidad, Profesor

with app.app_context():
    # Crear grupos
    grupos = [
        Grupo(nombre="Grupo A"),
        Grupo(nombre="Grupo B"),
    ]
    db.session.add_all(grupos)

    # Crear carreras
    carreras = [
        Carrera(nombre="Ingeniería en Sistemas"),
        Carrera(nombre="Medicina"),
    ]
    db.session.add_all(carreras)

    # Crear universidades
    universidades = [
        Universidad(nombre="Universidad Nacional"),
        Universidad(nombre="Universidad de Buenos Aires"),
    ]
    db.session.add_all(universidades)

    # Crear profesores
    profesores = [
        Profesor(nombre="Juan Pérez"),
        Profesor(nombre="María Gómez"),
    ]
    db.session.add_all(profesores)

    # Guardar cambios en la base de datos
    db.session.commit()
    print("Datos iniciales creados correctamente.")