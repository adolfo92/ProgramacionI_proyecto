# logica.py

import sqlite3

# miConexion = sqlite3.connect("./Databases/listaAlumnos")
# miCursor = miConexion.cursor()


class ListaAlumnos:

	alumnos = []

	def __init__(self):
		# Inicia conexion con base de datos
		miConexion = sqlite3.connect("./Databases/listaAlumnos")
		miCursor = miConexion.cursor()

		# Creo Tabla a trabajar
		try:
			miCursor.execute('''
				CREATE TABLE ALUMNOS(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				NOMBRE VARCHAR(20),
				APELLIDO VARCHAR(20),
				CEDULA INTEGER UNIQUE)
				''')
		except:
			print("Se accedio a la tabla ALUMNOS")

		# Cargo el conenido de la tabla a la lista "alumnos"
		miCursor.execute("SELECT * FROM ALUMNOS")
		self.alumnos = miCursor.fetchall()

		# Cierra la conexion
		miConexion.close()

	def actualizaLista(self):
		# Inicia conexion con base de datos
		miConexion = sqlite3.connect("./Databases/listaAlumnos")
		miCursor = miConexion.cursor()

		# Cargo el conenido actualizado de la lista a la lista "alumnos"
		miCursor.execute("SELECT * FROM ALUMNOS")
		self.alumnos = miCursor.fetchall()

		# Cierra la conexion
		miConexion.close()

	def agregaPersonas(self, nombre, apellido, cedula):
		# Inicia conexion con base de datos
		miConexion = sqlite3.connect("./Databases/listaAlumnos")
		miCursor = miConexion.cursor()

		# Agrega personas y me actualiza la lista del objeto de una vez
		try:
			miCursor.execute(f"INSERT INTO ALUMNOS VALUES (NULL,?,?,?)", (nombre, apellido, cedula))
		except:
			return 0
		miConexion.commit()
		# Cierra la conexion
		miConexion.close()
		self.actualizaLista()

	def eliminaPersonas(self, cedula):
		# Inicia conexion con base de datos
		miConexion = sqlite3.connect("./Databases/listaAlumnos")
		miCursor = miConexion.cursor()

		# Elimina personas y me actualiza la lista del objeto de una vez
		miCursor.execute(f"DELETE FROM ALUMNOS WHERE CEDULA=" + str(cedula))
		miConexion.commit()
		self.actualizaLista()

		# Cierra la conexion
		miConexion.close()

	def modificaPersonas(self, cedula, campo, nuevoValor):
		# Inicia conexion con base de datos
		miConexion = sqlite3.connect("./Databases/listaAlumnos")
		miCursor = miConexion.cursor()

		# Modifica personas y me actualiza la tabla del objeto de una vez
		miCursor.execute(f"UPDATE ALUMNOS SET {campo}=? WHERE CEDULA=?", (nuevoValor, cedula))
		miConexion.commit()
		self.actualizaLista()

		# Cierra la conexion
		miConexion.close()

	def dameTabla(self):
		# Me retorna el objeto lista
		return self.alumnos



