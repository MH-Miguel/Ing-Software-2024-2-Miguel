# from flask import Blueprint, request, render_template, flash, redirect, url_for
# #tengo que importarlo de forma correcta:
# from ..models import db, Usuario

# usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

# # CRUD - Crear Usuario
# @usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
# def agregar_usuario():
#     if request.method == 'GET':
#         return render_template('agregar_usuario.html')
#     else:
#         # Obtener la información del formulario
#         nombre = request.form['nombre']
#         ap_pat = request.form['ap_pat']
#         ap_mat = request.form['ap_mat']
#         email = request.form['email']
#         password = request.form['password']

#         # Crear una nueva instancia de Usuario
#         nuevo_usuario = Usuario(nombre=nombre, apPat=ap_pat, apMat=ap_mat, email=email, password=password)

#         # Guardar el nuevo usuario en la base de datos
#         db.session.add(nuevo_usuario)
#         db.session.commit()

#         flash('Usuario agregado correctamente', 'success')
#         return redirect(url_for('usuario.ver_usuarios'))

# # CRUD - Leer Usuario
# @usuario_blueprint.route('/')
# def ver_usuarios():
#     usuarios = Usuario.query.all()
#     return render_template('ver_usuarios.html', usuarios=usuarios)

# # CRUD - Actualizar Usuario
# @usuario_blueprint.route('/editar/<int:id_usuario>', methods=['GET', 'POST'])
# def editar_usuario(id_usuario):
#     usuario = Usuario.query.get_or_404(id_usuario)
#     if request.method == 'GET':
#         return render_template('editar_usuario.html', usuario=usuario)
#     else:
#         # Obtener la información del formulario
#         usuario.nombre = request.form['nombre']
#         usuario.apPat = request.form['ap_pat']
#         usuario.apMat = request.form['ap_mat']
#         usuario.email = request.form['email']

#         # Guardar los cambios en la base de datos
#         db.session.commit()

#         flash('Usuario actualizado correctamente', 'success')
#         return redirect(url_for('usuario.ver_usuarios'))

# # CRUD - Eliminar Usuario
# @usuario_blueprint.route('/eliminar/<int:id_usuario>', methods=['POST'])
# def eliminar_usuario(id_usuario):
#     usuario = Usuario.query.get_or_404(id_usuario)
#     db.session.delete(usuario)
#     db.session.commit()
#     flash('Usuario eliminado correctamente', 'success')
#     return redirect(url_for('usuario.ver_usuarios'))

from flask import Blueprint, request, render_template, flash, redirect, url_for
from ..models import Rentar, db, Usuario

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

# CRUD - Agregar Usuario
@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('usuario/agregar_usuario.html')
    else:
        # Obtener la información del formulario
        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        email = request.form['email']
        password = request.form['password']

        # Crear una nueva instancia de Usuario
        nuevo_usuario = Usuario(nombre=nombre, apPat=ap_pat, apMat=ap_mat, email=email, password=password)

        # Guardar el nuevo usuario en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario agregado correctamente', 'success')
        return redirect(url_for('usuario.ver_usuarios'))

# CRUD - Ver Usuarios
@usuario_blueprint.route('/ver')
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/ver_usuarios.html', usuarios=usuarios)

# CRUD - Editar Usuario
@usuario_blueprint.route('/editar/<int:id_usuario>', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    if request.method == 'POST':
        # Obtener la información del formulario
        usuario.nombre = request.form['nombre']
        usuario.apPat = request.form['ap_pat']
        usuario.apMat = request.form['ap_mat']
        usuario.email = request.form['email']

        # Guardar los cambios en la base de datos
        db.session.commit()

        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('usuario.ver_usuarios'))
    else:
        return render_template('usuario/editar_usuario.html', usuario=usuario)

# CRUD - Eliminar Usuario
@usuario_blueprint.route('/eliminar/<int:id_usuario>', methods=['POST'])
# def eliminar_usuario(id_usuario):
#     usuario = Usuario.query.get_or_404(id_usuario)
#     db.session.delete(usuario)
#     db.session.commit()
#     flash('Usuario eliminado correctamente', 'success')
#     return redirect(url_for('usuario.ver_usuarios'))
def eliminar_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)

    # Obtener todas las rentas asociadas al usuario
    rentas_usuario = Rentar.query.filter_by(idUsuario=id_usuario).all()

    # Eliminar las rentas asociadas al usuario
    for renta in rentas_usuario:
        db.session.delete(renta)

    # Eliminar el usuario
    db.session.delete(usuario)

    # Confirmar y realizar los cambios en la base de datos
    db.session.commit()

    flash('Usuario y rentas asociadas eliminadas correctamente', 'success')
    return redirect(url_for('usuario.ver_usuarios'))