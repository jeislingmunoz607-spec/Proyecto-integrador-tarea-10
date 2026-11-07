from data.conexion import obtener_conexion

try:
    conexion = obtener_conexion()

    if conexion.is_connected():
        print("Conexión exitosa con la base de datos")

    conexion.close()

except Exception as error:
    print("Error de conexión:", error)
