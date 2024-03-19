from flask import Blueprint, request, render_template, flash, redirect, url_for
#ver si funciona la ruta
from ..models import db, Pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

# CRUD - Crear Película
@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('pelicula/agregar_pelicula.html')
    else:
        # Obtener la información del formulario
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = int(request.form['duracion'])
        inventario = int(request.form.get('inventario', 1))

        # Crear una nueva instancia de Película
        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)

        # Guardar la nueva película en la base de datos
        db.session.add(nueva_pelicula)
        db.session.commit()

        flash('Película agregada correctamente', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))

# CRUD - Leer Película
@pelicula_blueprint.route('/ver')
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('pelicula/ver_peliculas.html', peliculas=peliculas)

# CRUD - Editar Película
@pelicula_blueprint.route('/editar/<int:id_pelicula>', methods=['GET', 'POST'])
def editar_pelicula(id_pelicula):
    pelicula = Pelicula.query.get_or_404(id_pelicula)
    if request.method == 'GET':
        return render_template('pelicula/editar_pelicula.html', pelicula=pelicula)
    else:
        # Obtener la información del formulario
        pelicula.nombre = request.form['nombre']
        pelicula.genero = request.form['genero']
        pelicula.duracion = int(request.form['duracion'])
        pelicula.inventario = int(request.form.get('inventario', 1))

        # Guardar los cambios en la base de datos
        db.session.commit()

        flash('Película actualizada correctamente', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))

# CRUD - Eliminar Película
@pelicula_blueprint.route('/eliminar/<int:id_pelicula>', methods=['POST'])
def eliminar_pelicula(id_pelicula):
    pelicula = Pelicula.query.get_or_404(id_pelicula)
    db.session.delete(pelicula)
    db.session.commit()
    flash('Película eliminada correctamente', 'success')
    return redirect(url_for('pelicula.ver_peliculas'))