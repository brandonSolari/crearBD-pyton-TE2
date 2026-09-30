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

#crear tabala mascota
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mascota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especie TEXT,
        dueno_id INTEGER,
        FOREIGN KEY (dueno_id) REFERENCES dueno(id)
    )
""")

# crear la tabla cita
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cita (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        motivo TEXT,
        mascota_id INTEGER,
        FOREIGN KEY (mascota_id) REFERENCES mascota(id)
    )
""")

#insertar datos a la tabal cita 
cursor.execute("INSERT INTO cita (fecha, motivo, mascota_id) VALUES ('2026-10-05', 'Vacuna', 1)")
cursor.execute("INSERT INTO cita (fecha, motivo, mascota_id) VALUES ('2026-10-07', 'Revisión', 2)")
cursor.execute("INSERT INTO cita (fecha, motivo, mascota_id) VALUES ('2026-10-10', 'Desparasitación', 3)")

conexion.commit()