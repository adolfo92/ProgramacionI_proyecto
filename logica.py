#logica.py
import sqlite3

miConexion = sqlite3.connect("./Databases/listaAlumnos")

miCursor = miConexion.cursor()

class ListaAlumnos:

	def __init__(self):

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



miConexion.close()