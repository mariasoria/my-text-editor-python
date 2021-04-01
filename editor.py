from tkinter import *
from tkinter import filedialog as FileDialog
from io import open


# definicion variables globales
ruta = "" # almacenara la ruta del fichero

# definicion de funciones
def new_file():
    global ruta # la definimos global xq queremos modificar cada vez la global
    mensaje.set("New file")
    ruta = ""
    texto.delete(1.0, "end") # borrara desde el caracter 1 del texto (siempre es un \n), hasta el final (end)
    root.title("My editor")


def open_file():
    global ruta
    mensaje.set("Open a file")
    ruta = FileDialog.askopenfilename(title="Open a file", filetypes=(("Text file", "*.txt"),))
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - My editor")

def save_file():
    mensaje.set("Save file")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c") 
        # "end-1c" recupera todo el texto excepto el salto de linea del 
        # final, para que cada vez que lo abra no me añada un salto de linea
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File saved succesfully")
    else: # si el fichero no existe, entonces se guarda un archivo nuevo
        save_file_as()

def save_file_as():
    global ruta
    mensaje.set("Save file as:")
    fichero = FileDialog.asksaveasfile(title="Save a new file", mode='w', defaultextension=".txt")
    # nos devuelve un fichero ya abierto o None
    if fichero is not None:
        ruta = fichero.name # .name:  Nos dice la ruta del fichero
        contenido = texto.get(1.0, "end-1c") 
        # "end-1c" recupera todo el texto excepto el salto de linea del 
        # final, para que cada vez que lo abra no me añada un salto de linea
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File created succesfully")
    else:
        mensaje.set("Saving operation cancelled")
        ruta = ""

root = Tk()
root.title("My editor")

# Crear menubar
menubar = Menu(root)

# Añadir a root la barra de menu
root.config(menu=menubar)
filemenu = Menu(menubar)

filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as...", command=save_file_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Añadir los submenus al menu
menubar.add_cascade(label="File", menu = filemenu)

#añadimos una caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=6, font=("Museo Slab", 12))

# Creamos una label para hacer un monitor inferior
mensaje = StringVar()
mensaje.set("Welcome to your editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.mainloop()