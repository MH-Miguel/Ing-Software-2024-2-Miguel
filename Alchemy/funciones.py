from clasesAlchemy import db
from clasesAlchemy.modelos import Usuario, Pelicula, Rentar
from sqlalchemy.exc import IntegrityError



def ver_registros(tabla):
    registros = tabla.query.all()
    if not registros:
        print("No hay registros en la tabla.")
        return
    
    for registro in registros:
        # Obtener los atributos del registro como un diccionario
        atributos = registro.__dict__

        # Eliminar atributos internos que no queremos mostrar
        atributos.pop("_sa_instance_state")

        # Imprimir los atributos
        print("Registro:")
        for key, value in atributos.items():
            print(f"{key}: {value}")
        print()

def filtrar_por_idUsuario(tabla, id):
    registro = tabla.query.filter_by(idUsuario=id)
    registroF = tabla.query.filter_by(idUsuario=id).first()
    if registroF:
        for registros in registro:
            atributos = registros.__dict__
            atributos.pop("_sa_instance_state")
            print("Registro:")
            for key, value in atributos.items():
                print(f"{key}: {value}")
            print()
    else:
        print("No se encontró ningún registro con ese ID.")

def filtrar_por_idPelicula(tabla, id):
    
    registro = tabla.query.filter_by(idPelicula=id)
    registroF = tabla.query.filter_by(idPelicula=id).first()
    if registroF:
        for registros in registro:
            atributos = registros.__dict__
            atributos.pop("_sa_instance_state")
            print("Registro:")
            for key, value in atributos.items():
                print(f"{key}: {value}")
            print()
    else:
        print("No se encontró ningún registro con ese ID.")

def filtrar_por_idRentar(tabla, id):
    
    registro = tabla.query.filter_by(idRentar=id)
    registroF = tabla.query.filter_by(idRentar=id).first()
    if registroF:
        for registros in registro:
            atributos = registros.__dict__
            atributos.pop("_sa_instance_state")
            print("Registro:")
            for key, value in atributos.items():
                print(f"{key}: {value}")
            print()
    else:
        print("No se encontró ningún registro con ese ID.")

def actualizar_nombre(tabla, id, nuevo_nombre):
    registro = tabla.query.get(id)
    if registro:
        registro.nombre = nuevo_nombre
        db.session.commit()
        print("Nombre actualizado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

def actualizar_fecha_renta(id_rentar, nueva_fecha):
    renta = Rentar.query.get(id_rentar)
    if renta:
        renta.fecha_renta = nueva_fecha
        db.session.commit()
        print("Fecha de renta actualizada correctamente.")
    else:
        print("No se encontró ninguna renta con ese ID.")

def eliminar_registro(tabla, id=None):
    if id:
        try:
            if (tabla == Usuario) | (tabla == Pelicula):
            # Eliminar los registros de la tabla 'Rentar' asociados al usuario a eliminar
                Rentar.query.filter_by(idUsuario=id).delete()
                db.session.commit()
            
            registro = tabla.query.get(id)
            if registro:
                db.session.delete(registro)
                db.session.commit()
                print("Registro eliminado correctamente.")
            else:
                print("No se encontró ningún registro con ese ID.")
        except IntegrityError as e:
            db.session.rollback()
            print("Error de integridad referencial:", e)
    else:
        try:
            if (tabla == Usuario) | (tabla == Pelicula):
                # Eliminar los registros relacionados en la tabla 'rentar'
                Rentar.query.delete()
                db.session.commit()
            
            # Eliminar los registros de la tabla especificada
            tabla.query.delete()
            db.session.commit()
            print("Registros eliminados correctamente.")
        except IntegrityError as e:
            db.session.rollback()
            print("Error de integridad referencial:", e)