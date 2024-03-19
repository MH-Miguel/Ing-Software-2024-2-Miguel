from flask import Blueprint, request, render_template, flash, redirect, url_for
from datetime import datetime, timedelta
from sqlalchemy import func
from ..models import db, Rentar, Usuario, Pelicula

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

# CRU - Crear Renta
@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')
        id_pelicula = request.form.get('id_pelicula')
        dias_renta = request.form.get('dias_renta')

        # Verificar si el usuario y la película existen
        usuario = Usuario.query.get(id_usuario)
        pelicula = Pelicula.query.get(id_pelicula)

        if usuario is None:
            flash('El ID de usuario ingresado no existe.', 'error')
            return redirect(url_for('renta.agregar_renta'))
        
        if pelicula is None:
            flash('El ID de película ingresado no existe.', 'error')
            return redirect(url_for('renta.agregar_renta'))

        fecha_renta = datetime.now()  # Obtiene la fecha y hora actuales
        # Si ambos existen, proceder con la creación de la renta
        nueva_renta = Rentar(idUsuario=id_usuario, idPelicula=id_pelicula, fecha_renta=fecha_renta, dias_de_renta=dias_renta)
        db.session.add(nueva_renta)
        db.session.commit()

        flash('Renta creada correctamente.', 'success')
        return redirect(url_for('renta.ver_rentas'))

    return render_template('renta/agregar_renta.html')

# CRU - Leer Renta
@renta_blueprint.route('/ver')
def ver_rentas():
    # Obtener todas las rentas y marcar las vencidas
    rentas = Rentar.query.all()
    for renta in rentas:
        if renta.fecha_renta + timedelta(days=renta.dias_de_renta) < datetime.now():
            renta.vencida = True
        else:
            renta.vencida = False
    return render_template('renta/ver_rentas.html', rentas=rentas)

# CRU - Actualizar Renta
@renta_blueprint.route('/actualizar/<int:id_renta>', methods=['POST'])
def actualizar_renta(id_renta):
    renta = Rentar.query.get_or_404(id_renta)
    renta.estatus = not renta.estatus  # Cambiar el valor de entrega (marcado o desmarcado)
    db.session.commit()
    flash('Estado de la renta actualizado correctamente', 'success')
    return redirect(url_for('renta.ver_rentas'))