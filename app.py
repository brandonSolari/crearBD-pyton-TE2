import sqlite3
conexion = sqlite3.connect("veterinaria.db")
cursor = conexion.cursor()

# Crear tabla dueño
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dueno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT
    )
""")
#insertar datos
cursor.execute("INSERT INTO dueno (nombre, telefono) VALUES ('Juan Pérez', '70012345')")
cursor.execute("INSERT INTO dueno (nombre, telefono) VALUES ('María López', '71123456')")
cursor.execute("INSERT INTO dueno (nombre, telefono) VALUES ('Carlos Mamani', '72234567')")

conexion.commit()