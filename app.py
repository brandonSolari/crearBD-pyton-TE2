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


# isnertar datos en la tabla mascota
cursor.execute("INSERT INTO mascota (nombre, especie, dueno_id) VALUES ('Firulais', 'Perro', 1)")
cursor.execute("INSERT INTO mascota (nombre, especie, dueno_id) VALUES ('Misi', 'Gato', 2)")
cursor.execute("INSERT INTO mascota (nombre, especie, dueno_id) VALUES ('Rocky', 'Perro', 3)")

conexion.commit()