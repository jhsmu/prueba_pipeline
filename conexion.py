
import os
import mysql.connector


db_host = os.environ.get('DB_HOST') 
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER') 
db_password = os.environ.get ('DB_PASSWORD') 
db_name = os.environ.get('DB_NAME')

# Configuración de la conexión y conexion a la base de datos y verificamos la conexion a la base de datos

try:
    conexion = mysql.connector.connect(  
    user = db_user,
    port = db_port,
    password = db_password,
    host = db_host,
    database = db_name)
    print("Conexión exitosa a la base de datos.")

    Mycursor = conexion.cursor()

    Mycursor.execute("SELECT * FROM administrador")

    consulta = Mycursor.fetchall()

    for consu in consulta:
        print(consu)

    # Cerrar la conexión
    conexion.close() 
except mysql.connector.Error as error:
    print("Error al conectar a la base de datos. {}".format(error))

