""" import tkinter as tk 
from tkinter import ttk


class Aplicacion:
  def __init__(self) -> None:
    self.valor = 1
    self.ventana1 = tk.Tk()
    self.ventana1.title("Controles Buttol y Label")
    
    self.label1 = ttk.Label(self.ventana1, text=self.valor)
    self.label1.grid(column=0, row=0)
    self.label1.configure(foreground="red")

    self.boton1 = ttk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
    self.boton1.grid(column=0, row=1)

    self.boton2 = ttk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
    self.boton2.grid(column=0, row=2)
    
    self.ventana1.mainloop()


  def incrementar(self):
    self.valor = self.valor + 1
    self.label1.config(text=self.valor)

  def decrementar(self):
    self.valor = self.valor - 1
    self.label1.config(text=self.valor)
    
aplicacion = Aplicacion() """

import tkinter as tk 
from tkinter import ttk 

""" class Aplicacion:
  
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.label1 = ttk.Label(text="Ingrese nombre de usuario: ")
    self.label1.grid(column=0, row=0)
    self.data1 = tk.StringVar()
    self.entry1 = ttk.Entry(self.ventana1, width=30, textvariable=self.data1)
    self.entry1.grid(column=1, row=0)
    
    self.label2 = ttk.Label(text="Ingrese clave:")
    self.label2.grid(column=0, row=1)
    self.data2 = tk.StringVar()
    self.entry2 = ttk.Entry(self.ventana1, width=30, textvariable=self.data2, show="*")
    self.entry2.grid(column=1, row=1)

    self.boton1 = ttk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
    self.boton1.grid(column=1, row=2)
    
    self.ventana1.mainloop()
  
  def ingresar(self):
    if self.data1.get() == "Alex" and self.data2.get() == "abc123":
      self.ventana1.title("CORRECTO")
    else:
      self.ventana1.title("INCORRECTO")
      
aplicacion = Aplicacion() """


""" class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.seleccion = tk.IntVar()
    self.seleccion.set(2)
    
    self.radio1 = ttk.Radiobutton(self.ventana1, text="Varon", variable=self.seleccion, value=1)
    self.radio1.grid(column=0, row=0)
    
    self.radio2 = ttk.Radiobutton(self.ventana1, text="Mujer", variable=self.seleccion, value=2)
    self.radio2.grid(column=0, row=1)

    self.boton1 = ttk.Button(self.ventana1, text="Mostrar seleccionado", command=self.mostrarseleccionado)
    self.boton1.grid(column=0, row=2)

    self.label1 = ttk.Label(text="Opcion seleccionada")
    self.label1.grid(column=0, row=3)

    self.ventana1.mainloop()
    
  def mostrarseleccionado(self):
    if self.seleccion.get() == 1:
      self.label1.configure(text="Opcion seleccionado: Varon")
    if self.seleccion.get() == 2:
      self.label1.configure(text="Opcion seleccionado: Mujer")


aplicacion = Aplicacion() """



""" class Aplicacion:
  
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.ventana1.title("Conteo de seleccion")
    
    self.seleccion1 = tk.IntVar()
    self.ckeck1 = ttk.Checkbutton(self.ventana1, text="Python", variable=self.seleccion1)
    self.ckeck1.grid(column=0, row=0)

    self.seleccion2 = tk.IntVar()
    self.ckeck2 = ttk.Checkbutton(self.ventana1, text="C++", variable=self.seleccion2)
    self.ckeck2.grid(column=0, row=1)
    
    self.seleccion3 = tk.IntVar()
    self.ckeck3 = ttk.Checkbutton(self.ventana1, text="Java", variable=self.seleccion3)
    self.ckeck3.grid(column=0, row=2)

    self.boton1 = ttk.Button(self.ventana1, text="Verificar", command=self.verificar)
    self.boton1.grid(column=0, row=4)

    self.label1 = ttk.Label(text="cantidad: ")
    self.label1.grid(column=0, row=5)

    self.ventana1.mainloop()
    
  def verificar(self):
    cant = 0
    if self.seleccion1.get() == 1:
      cant += 1
      
    if self.seleccion2.get() == 1:
      cant += 1
      
    if self.seleccion3.get() == 1:
      cant += 1
      
    
    self.label1.configure(text="cantidad:" + str(cant))


aplicacion = Aplicacion() """


class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.listbox1 = tk.Listbox(self.ventana1)
    self.listbox1.grid(column=0, row=0)
    self.listbox1.insert(0, "papa")
    self.listbox1.insert(1, "manzana")
    self.listbox1.insert(2, "pera")
    self.listbox1.insert(3, "sandia")
    self.listbox1.insert(4, "naranja")
    self.listbox1.insert(5, "melon")
    
    self.boton1 = ttk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
    self.boton1.grid(column=0, row=1)

    self.label1 = ttk.Label(text="Seleccionado: ")
    self.label1.grid(column=0, row=2)

    self.ventana1.mainloop()

  def recuperar(self):
    if len(self.listbox1.curselection()) != 0:
      self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))
    
aplicacion = Aplicacion()
















































