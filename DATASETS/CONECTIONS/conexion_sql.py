import pymysql
import pandas as pd
# Local Host = 127.0.0.1

# Funcion para CONECTAR a la base de datos (MySQL)
def conectarBD(host, user, password, db):
    try:
        conn = pymysql.connect(host=host, user=user, password=password, db=db)
        return conn
    except Exception as e:
        print(e)
        return False
# Función para EJECUTAR una query para la base de datos

def ejecutarQuery(connector, query):
    try:
        cur = connector.cursor()
        cur.execute(query)
        output = cur.fetchall()
        return output
    except Exception as e:
        print(e)
        return False
    
# Función para CERRAR la conexión a la base de datos
def cerrarBD(conector):
    try:
        conector.close()
        return True
    except Exception as e:
        print(e)
        return False

# Gestión inicio codigo
if __name__ == "__main__":

    # Conectar
    conexion = conectarBD("127.0.0.1", "IMPELIA", "1234", "ml-tests")
    if conexion:
        print(" [+] Conectado a la base de datos")

        # Extraer todos los datos de la base de datos
        data = ejecutarQuery(conexion, "SELECT * FROM restaurant_revenue")
        if data:
            # print(data) - Este print sirve para verificar que hay datos en la base de datos al principio.
            df = pd.DataFrame(data)
            print(df.head(10))
        else:
            print(" [-] Error de ejecución")

        # Desconectar
        close = cerrarBD(conexion)
        if close:
            print(" [+] Desconectados de la base de datos")
        else:
            print(" [-] Error al desconectar la conexión a la base de datos")
    else:
        print(" [-] Error al conectar a la base de datos")