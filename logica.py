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




	def agregaPersonas():
		return

	def eliminaPersonas():
		return

	def modificaPersonas():
		return

	def muestraTabla():
		return

miNuevaLista = ListaAlumnos()

miConexion.close()
