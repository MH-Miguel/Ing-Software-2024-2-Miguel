import pymysql.cursors
from datetime import datetime, timedelta
import random
import string

connection = pymysql.connect(host = 'localhost', 
                            user = 'lab',
                            password='Developer123!',
                            database='lab_ing_software',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
""""
try: 
    with connection.cursor() as cursor:
        sql= "INSERT INTO peliculas(idPelicula, nombre, genero, duracion, inventario) values('1', 'Ironman', 'ficcion', 95, '3')"
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()"""

def generar_email():
    dominio = "@gmail.com"  # Dominio de ejemplo, puedes cambiarlo según tus necesidades
    letras = string.ascii_lowercase
    nombre = ''.join(random.choice(letras) for _ in range(8))  # Generar una cadena aleatoria de 8 caracteres
    email = nombre + dominio
    return email

def insertar_registros():
    try:
        with connection.cursor() as cursor:
            # Insertar usuario
            sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, ('Miguel', 'Martinez', 'Herrera', 'contraseña123', generar_email()))
            connection.commit() 
            # Obtener el idUsuario recién insertado
            id_usuario = cursor.lastrowid

            # Insertar película
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Titanic', 'Romance', 195, 10))
            id_pelicula = cursor.lastrowid
            # Insertar renta
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta) VALUES (%s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_pelicula, datetime.now()-timedelta(days=5)))

        connection.commit()
        print("Registros insertados correctamente.")
    except Exception as e:
        print("Error al insertar registros:", e)

def filtrar_apellido(apellido):
    try:
        with connection.cursor() as cursor:
            # Consulta SQL para seleccionar usuarios cuyo apellido paterno o materno contenga la cadena dada
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
            apellido_like = '%' + apellido  # Añade '%' al final de la cadena para que coincida con apellidos que comiencen con la cadena dada
            cursor.execute(sql, (apellido_like, apellido_like))
            
            # Obtener resultados de la consulta
            result = cursor.fetchall()
            
            if result:  # Si se encontraron resultados
                for row in result:
                    print(row)
            else:
                print("No se encontraron usuarios con el apellido que termina en:", apellido)
    except Exception as e:
        print("Error al filtrar usuarios por apellido:", e)

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    try:
        with connection.cursor() as cursor:
            # Verificar si la película existe
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql, (nombre_pelicula,))
            result = cursor.fetchone()
            if result:
                # Actualizar el género de la película
                sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql, (nuevo_genero, nombre_pelicula))
                connection.commit()
                print("Género de la película actualizado correctamente.")
            else:
                print("La película no existe.")
    except Exception as e:
        print("Error al cambiar el género de la película:", e)

def eliminar_rentas_antiguas():
    try:
        with connection.cursor() as cursor:
            # Calcular la fecha límite
            fecha_limite = datetime.now() - timedelta(days=3)

            # Eliminar las rentas anteriores a la fecha límite
            sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql, (fecha_limite,))
            connection.commit()
            print("Rentas antiguas eliminadas correctamente.")
    except Exception as e:
        print("Error al eliminar rentas antiguas:", e)

# Ejecutar las funciones
insertar_registros()
# filtrar_apellido('omez')
# cambiar_genero_pelicula('Titanic', 'Drama')
# eliminar_rentas_antiguas()

# Cerrar la conexión
connection.close()