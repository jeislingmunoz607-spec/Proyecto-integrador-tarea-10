
from data.conexion import obtener_conexion


def obtener_reportes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT r.numero, e.codigo AS equipo, r.categoria,
               r.descripcion, r.estado, r.fecha, r.solucion
        FROM reportes r
        INNER JOIN equipos e ON r.id_equipo = e.id_equipo
        ORDER BY r.id_reporte DESC
    """)

    reportes = cursor.fetchall()

    cursor.close()
    conexion.close()

    for reporte in reportes:
        reporte["fecha"] = reporte["fecha"].strftime("%d/%m/%Y")

    return reportes


def buscar_reporte(numero):
    reportes = obtener_reportes()

    for reporte in reportes:
        if reporte["numero"] == numero:
            return reporte

    return None


def guardar_reporte(reporte):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id_equipo FROM equipos WHERE codigo = %s",
        (reporte["equipo"],)
    )

    equipo = cursor.fetchone()

    if equipo is None:
        cursor.close()
        conexion.close()
        raise ValueError("El equipo no está registrado en la base de datos")

    cursor.execute("""
        INSERT INTO reportes
        (numero, id_equipo, categoria, descripcion, estado, fecha, solucion)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        reporte["numero"],
        equipo[0],
        reporte["categoria"],
        reporte["descripcion"],
        reporte["estado"],
        reporte["fecha"],
        reporte["solucion"]
    ))

    conexion.commit()
    cursor.close()
    conexion.close()


def actualizar_solucion(numero, solucion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE reportes
        SET solucion = %s, estado = 'Resuelto'
        WHERE numero = %s
    """, (solucion, numero))

    actualizado = cursor.rowcount > 0

    conexion.commit()
    cursor.close()
    conexion.close()

    return actualizado
