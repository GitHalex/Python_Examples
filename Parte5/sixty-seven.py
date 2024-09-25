import tkinter as tk 
from tkinter import ttk 

""" class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.labelframe1 = ttk.LabelFrame(self.ventana1, text="Login")
    self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
    self.login()
    self.labelframe2 = ttk.LabelFrame(self.ventana1, text="Operaciones")
    self.labelframe2.grid(column=0, row=1, padx=5, pady=10)
    self.operaciones()
    self.ventana1.mainloop()
    
  def login(self):
    self.label1 = ttk.Label(self.labelframe1, text="Nombre de usuarios:")
    self.label1.grid(column=0, row=0, padx=4, pady=4)
    self.entry1 = tk.Entry(self.labelframe1)
    self.entry1.grid(column=1, row=0, padx=4, pady=4)
    
    self.label2 = ttk.Label(self.labelframe1, text="Ingrese clave:")
    self.label2.grid(column=0, row=1, padx=4, pady=4)
    self.entry2 = tk.Entry(self.labelframe1, show="*")
    self.entry2.grid(column=1, row=1, padx=4, pady=4)

    self.boton1 = ttk.Button(self.labelframe1, text="Ingresar")
    self.boton1.grid(column=1, row=2, padx=4, pady=4)

  def operaciones(self):
    self.boton2 = ttk.Button(self.labelframe1, text="Agregar usuario")
    self.boton2.grid(column=0, row=3, padx=8, pady=10)
    self.boton3 = ttk.Button(self.labelframe1, text="Modificar usuario")
    self.boton3.grid(column=1, row=3, padx=8, pady=10)
    self.boton4 = ttk.Button(self.labelframe1, text="Borrar usuario")
    self.boton4.grid(column=2, row=3, padx=8, pady=10)

aplicacion = Aplicacion() """

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    #El primer label que se va hacer para el articulo
    self.labelframe1 = ttk.LabelFrame(self.ventana1, text="ARTICULO")
    self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
    self.articulos()
    #El primer label que se va hacer para operaciones
    self.labelframe2 = ttk.LabelFrame(self.ventana1, text="OPERACIONES")
    self.labelframe2.grid(column=0, row=1, padx=5, pady=10)
    self.operaciones()
    
    self.ventana1.mainloop()

  def articulos(self):
    self.label1 = ttk.Label(self.labelframe1, text="Codigo del articulo: ")
    self.label1.grid(column=0, row=0, padx=4, pady=4)
    self.entry1 = ttk.Entry(self.labelframe1)
    self.entry1.grid(column=1, row=0, padx=4, pady=4)
    
    self.label2 = ttk.Label(self.labelframe1, text="Descripcion: ")
    self.label2.grid(column=0, row=1, padx=4, pady=4)
    self.entry2 = ttk.Entry(self.labelframe1)
    self.entry2.grid(column=1, row=1, padx=4, pady=4)
    
    self.label3 = ttk.Label(self.labelframe1, text="Precio: ")
    self.label3.grid(column=0, row=2, padx=4, pady=4)
    self.entry3 = ttk.Entry(self.labelframe1)
    self.entry3.grid(column=1, row=2, padx=4, pady=4)

  def operaciones(self):
    self.boton2 = ttk.Button(self.labelframe2, text="Alta")
    self.boton2.grid(column=0, row=3, padx=8, pady=10)
    self.boton3 = ttk.Button(self.labelframe2, text="Baja")
    self.boton3.grid(column=1, row=3, padx=8, pady=10)
    self.boton4 = ttk.Button(self.labelframe2, text="Modificacion")
    self.boton4.grid(column=2, row=3, padx=8, pady=10)
    
aplicacion = Aplicacion()
