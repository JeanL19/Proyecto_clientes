import mysql.connector

conexion = mysql.connector.connect(
    user="root",
    host="localhost",
    password="12345678",
    database="proyecto",
    port="3306"
)


cursor = conexion.cursor()

print(conexion)

