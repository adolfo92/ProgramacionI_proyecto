# logica.py

import sqlite3

miConexion = sqlite3.connect("./Databases/listaAlumnos")

miCursor = miConexion.cursor()


class ListaAlumnos:

	alumnos = []

	def __init__(self):
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

	def actualizaLista(self):
		# Cargo el conenido actualizado de la lista a la lista "alumnos"
		miCursor.execute("SELECT * FROM ALUMNOS")
		self.alumnos = miCursor.fetchall()

	def agregaPersonas(self, nombre, apellido, cedula):
		# Agrega personas y me actualiza la lista del objeto de una vez
		try:
			miCursor.execute(f"INSERT INTO ALUMNOS VALUES (NULL,?,?,?)", (nombre, apellido, cedula))
		except:
			return 0
		miConexion.commit()
		self.actualizaLista()

	def eliminaPersonas(self, cedula):
		# Elimina personas y me actualiza la lista del objeto de una vez
		print("DELETE FROM ALUMNOS WHERE CEDULA=" + str(cedula))
		miCursor.execute(f"DELETE FROM ALUMNOS WHERE CEDULA=" + str(cedula))
		miConexion.commit()
		self.actualizaLista()

	def modificaPersonas(self, cedula, campo, nuevoValor):
		# Modifica personas y me actualiza la tabla del objeto de una vez
		miCursor.execute(f"UPDATE ALUMNOS SET {campo}=? WHERE CEDULA=?", (nuevoValor, cedula))
		miConexion.commit()
		self.actualizaLista()

	def dameTabla(self):
		# Me retorna el objeto lista
		return self.alumnos


miNuevaLista = ListaAlumnos()


print(miNuevaLista.dameTabla())


miConexion.close()
