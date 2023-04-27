#-------------------------------
#desktop app no.1
#-------------------------------

#se importa la libreria tkinter con todas sus funciones
from tkinter import *

#-------------------------------
#fuciones de la app
#-------------------------------

#-------------------------------
#ventana principal de la app
#-------------------------------

#se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto TK()
ventana_principal = Tk()


# titulo de la ventana
ventana_principal.title("especialidad en sisitemas guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x500")

#run 
ventana_principal.mainloop()

#deshabilitar boton de maximisar
ventana_principal.resizable(False, False)

#color de fondo de la ventana
ventana_principal.config(bg="white")

#run
ventana_principal.mainloop()
