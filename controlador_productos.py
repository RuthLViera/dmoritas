import pymysql

def obtener_conexion():
    return pymysql.connect(host='sql10.freesqldatabase.com',
                                user='sql10507526',
                                password='njH1Njd5Pc',
                                db='sql10507526')

def insertar_producto(codigo, descripcion, imagen, categoria, precio, cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos (codigo, descripcion, imagen, categoria, precio, cantidad) VALUES (%s, %s, %s, %s, %s, %s)",
                       (codigo, descripcion, imagen, categoria, precio, cantidad))
    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = obtener_conexion()
    producto = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT pid, codigo, descripcion, imagen, categoria, precio, cantidad FROM productos")
        producto = cursor.fetchall()
    conexion.close()
    return producto


def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE pid = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT pid, codigo, descripcion, imagen, categoria, precio, cantidad FROM productos WHERE pid = %s", (id,))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_producto(codigo, descripcion, imagen, categoria, precio, cantidad, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET codigo = %s, descripcion = %s, imagen = %s, categoria = %s, precio = %s, cantidad = %s WHERE pid = %s",
                       (codigo, descripcion, imagen, categoria, precio, cantidad, id))
    conexion.commit()
    conexion.close()
