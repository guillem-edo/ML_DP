import pymysql

# Funcion para conectar a la base de datos (MySQL)
# Local Host = 127.0.0.1
def conectarBD():
    try:
        conexion = pymysql.connect(host="localhost", user="IMPELIA", passwd="<1234>", db="ml-tests")
        return conexion
    except:
        print("Error al conectar a la base de datos")
        exit()

# Gestión inicio codigo
if __name__ == "__main__":
    conexion = conectarBD()
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE prueba")
    conexion.commit()
    conexion.close()