from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Alumno, Grupo, Carrera, Universidad, Profesor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'tu_clave_secreta_aqui'

db.init_app(app)

# Crear la base de datos (solo la primera vez)
with app.app_context():
    db.create_all()

# Ruta principal (Read)
@app.route('/')
def index():
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

# Ruta para agregar un alumno (Create)
@app.route('/add_alumno', methods=['GET', 'POST'])
def add_alumno():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        grupo_id = request.form.get('grupo_id')
        carrera_id = request.form.get('carrera_id')
        universidad_id = request.form.get('universidad_id')
        profesor_id = request.form.get('profesor_id')

        if not nombre or not apellido:
            flash('Nombre y apellido son obligatorios', 'error')
            return redirect(url_for('add_alumno'))

        nuevo_alumno = Alumno(
            nombre=nombre,
            apellido=apellido,
            grupo_id=grupo_id,
            carrera_id=carrera_id,
            universidad_id=universidad_id,
            profesor_id=profesor_id
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        flash('Alumno agregado correctamente', 'success')
        return redirect(url_for('index'))
    
    grupos = Grupo.query.all()
    carreras = Carrera.query.all()
    universidades = Universidad.query.all()
    profesores = Profesor.query.all()
    return render_template('add_alumno.html', grupos=grupos, carreras=carreras, universidades=universidades, profesores=profesores)

# Ruta para editar un alumno (Update)
@app.route('/edit_alumno/<int:id>', methods=['GET', 'POST'])
def edit_alumno(id):
    alumno = Alumno.query.get_or_404(id)
    if request.method == 'POST':
        alumno.nombre = request.form.get('nombre')
        alumno.apellido = request.form.get('apellido')
        alumno.grupo_id = request.form.get('grupo_id')
        alumno.carrera_id = request.form.get('carrera_id')
        alumno.universidad_id = request.form.get('universidad_id')
        alumno.profesor_id = request.form.get('profesor_id')
        db.session.commit()
        flash('Alumno actualizado correctamente', 'success')
        return redirect(url_for('index'))
    
    grupos = Grupo.query.all()
    carreras = Carrera.query.all()
    universidades = Universidad.query.all()
    profesores = Profesor.query.all()
    return render_template('edit_alumno.html', alumno=alumno, grupos=grupos, carreras=carreras, universidades=universidades, profesores=profesores)

# Ruta para eliminar un alumno (Delete)
@app.route('/delete_alumno/<int:id>')
def delete_alumno(id):
    alumno = Alumno.query.get_or_404(id)
    db.session.delete(alumno)
    db.session.commit()
    flash('Alumno eliminado correctamente', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)