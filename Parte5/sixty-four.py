import tkinter as tk 
from tkinter import ttk 

""" class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.label1 = ttk.Label(self.ventana1, text="Seleccione un dia de la semana")
    self.label1.grid(column=0, row=0)

    self.opcion = tk.StringVar()
    diassemana = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
    self.combobox1 = ttk.Combobox(self.ventana1, width=10, textvariable=self.opcion, values=diassemana)

    self.combobox1.current(0)
    self.combobox1.grid(column=0, row=1)

    self.boton1 = tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
    self.boton1.grid(column=0, row=2)

    self.label2 = ttk.Label(self.ventana1, text="Dia seleccionado: ")
    self.label2.grid(column=0, row=3)

    self.ventana1.mainloop()

  def recuperar(self):
    self.label2.configure(text=self.opcion.get())

aplicacion = Aplicacion() """

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()

    self.label1 = ttk.Label(self.ventana1, text="nombre: ")
    self.label1.grid(column=0, row=0)

    self.nombre = tk.StringVar()
    self.entry1 = ttk.Entry(self.ventana1, width=20, textvariable=self.nombre)
    self.entry1.grid(column=1, row=0)
    
    self.label = ttk.Label(self.ventana1, text="pais: ")
    self.label.grid(column=0, row=1)
    
    self.opcion = tk.StringVar()
    paises = ["Bolivia","Chile","Peru","Paraguay","Brasil","Venezuela","Argentina","Colombia","Ecuador"]
    self.combobox1 = ttk.Combobox(self.ventana1, width=20, textvariable=self.opcion, values=paises)    
    self.combobox1.current(0)
    self.combobox1.grid(column=1, row=1)
    
    self.boton1 = tk.Button(self.ventana1, text="Dato seleccionado", command=self.recuperar)
    self.boton1.grid(column=0, row=2)
    
    self.label2 = ttk.Label(self.ventana1, text="nombre" )
    self.label2.grid(column=0, row=3)
    
    self.label3 = ttk.Label(self.ventana1, text="Pais seleccionado")
    self.label3.grid(column=1, row=3)
    
    self.ventana1.mainloop()
    
  def recuperar(self):
    self.label2.configure(text=self.nombre.get())
    self.label3.configure(text=self.opcion.get())
    

aplicacion = Aplicacion()
    