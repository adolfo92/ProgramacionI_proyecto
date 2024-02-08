# GUI.py
from tkinter import *
from logica import ListaAlumnos

ObjetoLista = ListaAlumnos()

# ---------------- Campo de variables

# ---------------- Campo de funciones


def campoDeAgregado():

	def agregameste():
		nombre = nombreEntry.get()
		apellido = apellidoEntry.get()
		cedula = cedulaEntry.get()

		ObjetoLista.agregaPersonas(nombre, apellido, cedula)

		frameAgregado.destroy()

		return print(f"Agregado:{nombre} {apellido}, cedula: {cedula}")

	global anchoDePantalla
	frameAgregado = Frame(raiz)
	frameAgregado.config(bg="#F3F3F3", height="200", width=anchoDePantalla, pady=5)
	frameAgregado.pack()

	labelTitulo = Label(frameAgregado, text="Agregar usuario")
	labelTitulo.grid(row=0, column=0, columnspan=3)

	# Nombre
	nombreLabel = Label(frameAgregado, text="Nombre")
	nombreLabel.grid(row=1, column=0)
	nombreEntry = Entry(frameAgregado)
	nombreEntry.grid(row=1, column=1)

	# Apellido
	apellidoLabel = Label(frameAgregado, text="Apellido")
	apellidoLabel.grid(row=2, column=0)
	apellidoEntry = Entry(frameAgregado)
	apellidoEntry.grid(row=2, column=1)

	# Cedula
	cedulaLabel = Label(frameAgregado, text="Cedula")
	cedulaLabel.grid(row=3, column=0)
	cedulaEntry = Entry(frameAgregado)
	cedulaEntry.grid(row=3, column=1)

	# Boton de enviado de datos

	botonEnviar = Button(frameAgregado, text="Enviar", command=agregameste)
	botonEnviar.grid(row=4, column=0, ipady=1)


def campoDeEliminacion():

	def eliminameste():
		cedula = cedulaEntry.get()

		ObjetoLista.eliminaPersonas(cedula)

		frameEliminado.destroy()

		return print(f"Eliminado usuario con cedula: {cedula}")

	global anchoDePantalla
	frameEliminado = Frame(raiz)
	frameEliminado.config(bg="#F3F3F3", height="100", width=anchoDePantalla, pady=5)
	frameEliminado.pack()

	labelTitulo = Label(frameEliminado, text="Eliminar usuario")
	labelTitulo.grid(row=0, column=0, columnspan=3)

	# Cedula
	cedulaLabel = Label(frameEliminado, text="Cedula")
	cedulaLabel.grid(row=1, column=0)
	cedulaEntry = Entry(frameEliminado)
	cedulaEntry.grid(row=1, column=1)

	botonEnviar = Button(frameEliminado, text="Enviar", command=eliminameste)
	botonEnviar.grid(row=2, column=0, ipady=1)


def campoDeModificado():

	def modificameste():

		# A modificar
		cedula = cedulaEntry.get()

		campos = [nombreModifEntry, apellidoModifEntry, cedulaModifEntry]

		nombreDeCampo = ["NOMBRE", "APELLIDO", "CEDULA"]

		i = 0

		for campo in campos:
			if campo.get() != "":
				print(campo.get())
				ObjetoLista.modificaPersonas(cedula, nombreDeCampo[i], campo.get())
			i += 1
		frameModificacion.destroy()

		return print(f"Modificado usuarion de cedula: {cedula}")

	global anchoDePantalla
	frameModificacion = Frame(raiz)
	frameModificacion.config(bg="#F3F3F3", height="100", width=anchoDePantalla, pady=5)
	frameModificacion.pack()

	labelTitulo = Label(frameModificacion, text="Modificar Usuario\n")
	labelTitulo.grid(row=0, column=0, columnspan=3)

	# Cedula para el target de modificacion
	cedulaLabel = Label(frameModificacion, text="Cedula del usuario a modificar")
	cedulaLabel.grid(row=1, column=0)
	cedulaEntry = Entry(frameModificacion)
	cedulaEntry.grid(row=1, column=1)

	# Espacio para datos a ser modificados (Tratar de no agregar mas pantallas)

	labelModificacion = Label(frameModificacion, text="Datos a modificar\n(solo modificar datos pertinentes)\n", justify="center")
	labelModificacion.grid(row=2, column=0, columnspan=3, pady=10)

	# Nombre a modificar
	nombreModifLabel = Label(frameModificacion, text="Nombre modificado")
	nombreModifLabel.grid(row=3, column=0, pady=10)
	nombreModifEntry = Entry(frameModificacion)
	nombreModifEntry.grid(row=3, column=1, pady=10)

	# Apellido a modificar
	apellidoModifLabel = Label(frameModificacion, text="Apellido modificado")
	apellidoModifLabel.grid(row=4, column=0)
	apellidoModifEntry = Entry(frameModificacion)
	apellidoModifEntry.grid(row=4, column=1)

	# Cedula a modificar
	cedulaModifLabel = Label(frameModificacion, text="Cedula modificada")
	cedulaModifLabel.grid(row=5, column=0)
	cedulaModifEntry = Entry(frameModificacion)
	cedulaModifEntry.grid(row=5, column=1)

	botonEnviar = Button(frameModificacion, text="Enviar", command=modificameste)
	botonEnviar.grid(row=6, column=0, ipady=1)


# ---------------- Campo de diseño


raiz = Tk()
raiz.config(bg="#F3F3F3")
raiz.resizable(False, False)


# ----------------------- FRAME PRINCIPAL ---------------------
framePrincipal = Frame(raiz)

framePrincipal.pack()

framePrincipal.config(bg="#F3F3F3", width="800", height="600")

# LABELS----------------------
labelOpciones = Label(framePrincipal, text="Opciones")
labelOpciones.grid(row=0, column=0)

labelBBDD = Label(framePrincipal, text="Visual de base de datos")
labelBBDD.grid(row=0, column=1)

# BOTONES---------------------
botonAgregar = Button(framePrincipal, text="Agregar", cursor="hand2", width=1,
	command=lambda: campoDeAgregado())
botonAgregar.grid(row=1, column=0, pady=20, padx=10)

botonEliminar = Button(framePrincipal, text="Eliminar", cursor="hand2", width=1,
	command=lambda: campoDeEliminacion())
botonEliminar.grid(row=2, column=0, pady=20, padx=10)

botonModificar = Button(framePrincipal, text="Modificar", cursor="hand2", width=1,
	command=lambda: campoDeModificado())
botonModificar.grid(row=3, column=0, pady=20, padx=10)

# VISUAL BBDD---------------------

displayBBDD = Frame(framePrincipal)
displayBBDD.config(bg="#FFFFFF", width="500")
displayBBDD.grid(row=1, rowspan=4, column=1, sticky="ns", padx=5, pady=5)

# --------- Datos varios para formato
anchoDePantalla = framePrincipal.winfo_width()


raiz.mainloop()
