from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from clasesAlchemy import db
from clasesAlchemy.modelos import Usuario, Pelicula, Rentar
from funciones import *
#from model.modelo_renta import eliminar_rentas_antiguas
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    
    with app.app_context():
        while True:
            print("\nMenú:")
            print("1. Ver registros de una tabla")
            print("2. Filtrar registros por ID")
            print("3. Actualizar nombre de un registro")
            print("4. Actualizar fecha de renta")
            print("5. Eliminar un registro por ID")
            print("6. Eliminar todos los registros")
            print("7. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                tabla = input("Ingresa el nombre de la tabla (usuario, pelicula, rentar): ").lower()
                if tabla == "usuario":
                    ver_registros(Usuario)
                elif tabla == "pelicula":
                    ver_registros(Pelicula)
                elif tabla == "rentar":
                    ver_registros(Rentar)
                else:
                    print("Tabla no válida.")
            
            elif opcion == "2":
                while True:
                    try:
                        tabla = input("Ingresa el nombre de la tabla (usuario, pelicula, rentar): ").lower()
                        if tabla not in {"usuario", "pelicula", "rentar"}:
                            raise ValueError("Tabla no válida.")
                        break  # Si el nombre de la tabla es válido, salimos del bucle
                    except ValueError as e:
                        print(e)
                while True:
                    try:
                        id = int(input("Ingresa el ID del registro a filtrar: "))
                        break  # Si la conversión a entero es exitosa, salimos del bucle
                    except ValueError:
                        print("Error: Por favor, ingresa un número entero válido.")
                if tabla == "usuario":
                    filtrar_por_idUsuario(Usuario, id)
                elif tabla == "pelicula":
                    filtrar_por_idPelicula(Pelicula, id)
                elif tabla == "rentar":
                    filtrar_por_idRentar(Rentar, id)
                
            
            elif opcion == "3":
                while True:
                    try:
                        tabla = input("Ingresa el nombre de la tabla (usuario, pelicula): ").lower()
                        if tabla not in {"usuario", "pelicula"}:
                            raise ValueError("Tabla no válida.")
                        break  # Si el nombre de la tabla es válido, salimos del bucle
                    except ValueError as e:
                        print(e)
                while True:
                    try:
                        id = int(input("Ingresa el ID del registro a actualizar: "))
                        break  # Si la conversión a entero es exitosa, salimos del bucle
                    except ValueError:
                        print("Error: Por favor, ingresa un número entero válido.")
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                if tabla == "usuario":
                    actualizar_nombre(Usuario, id, nuevo_nombre)
                elif tabla == "pelicula":
                    actualizar_nombre(Pelicula, id, nuevo_nombre)
                
            
            elif opcion == "4":
                while True:
                    try:
                        id_rentar = int(input("Ingresa el ID de la renta a actualizar: "))
                        break  # Si la conversión a entero es exitosa, salimos del bucle
                    except ValueError:
                        print("Error: Por favor, ingresa un número entero válido.")
                while True:
                    nueva_fecha_str = input("Ingresa la nueva fecha de renta (YYYY-MM-DD HH:MM:SS): ")
                    try:
                        nueva_fecha = datetime.strptime(nueva_fecha_str, "%Y-%m-%d %H:%M:%S")
                        break
                    except ValueError:
                        print("Error: La fecha proporcionada es inválida.")
                actualizar_fecha_renta(id_rentar, nueva_fecha)
            
            elif opcion == "5":
                while True:
                    try:
                        tabla = input("Ingresa el nombre de la tabla (usuario, pelicula, rentar): ").lower()
                        if tabla not in {"usuario", "pelicula", "rentar"}:
                            raise ValueError("Tabla no válida.")
                        break  # Si el nombre de la tabla es válido, salimos del bucle
                    except ValueError as e:
                        print(e)
                while True:
                    try:
                        id = int(input("Ingresa el ID del registro a eliminar: "))
                        break  # Si la conversión a entero es exitosa, salimos del bucle
                    except ValueError:
                        print("Error: Por favor, ingresa un número entero válido.")
                if tabla == "usuario":
                    eliminar_registro(Usuario, id)
                elif tabla == "pelicula":
                    eliminar_registro(Pelicula, id)
                elif tabla == "rentar":
                    eliminar_registro(Rentar, id)
                else:
                    print("Tabla no válida.")
            
            elif opcion == "6":
                while True:
                    try:
                        tabla = input("Ingresa el nombre de la tabla (usuario, pelicula, rentar): ").lower()
                        if tabla not in {"usuario", "pelicula", "rentar"}:
                            raise ValueError("Tabla no válida.")
                        break  # Si el nombre de la tabla es válido, salimos del bucle
                    except ValueError as e:
                        print(e)
                if tabla == "usuario":
                    eliminar_registro(Usuario)
                elif tabla == "pelicula":
                    eliminar_registro(Pelicula)
                elif tabla == "rentar":
                    eliminar_registro(Rentar)
                else:
                    print("Tabla no válida.")
            
            elif opcion == "7":
                print("Saliendo...")
                break
            
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    