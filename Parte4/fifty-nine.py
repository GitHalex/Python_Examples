""" import tkinter as tk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.label1=tk.Label(self.ventana1, text="Ingrese un numero: ")
    self.label1.grid(column=0, row=0)
    
    self.dato = tk.StringVar()
    self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato)
    self.entry1.grid(column=0, row=1)
    
    self.boton1 = tk.Button(self.ventana1, text="Calcular Cuadrado", command=self.calcularcuadrado)
    self.boton1.grid(column=0,row=2)

    self.label2 = tk.Label(self.ventana1, text="resultado")
    self.label2.grid(column=0, row=3)
    
    self.ventana1.mainloop()

  def calcularcuadrado(self):
    valor = int(self.dato.get())
    cuadrado = valor*valor
    self.label2.configure(text=cuadrado)


aplicacion = Aplicacion() """

""" import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0)
        
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)
        
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=1)
        
        self.ventana1.mainloop()

    def ingresar(self):
        self.ventana1.title(self.dato.get())

aplicacion1=Aplicacion()   """

import tkinter as tk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana = tk.Tk()
    self.label = tk.Label(self.ventana, text="Ingrese un numero 1: ")
    self.label.grid(column=0, row=0)

    self.dato = tk.StringVar()
    self.entry1 = tk.Entry(self.ventana, width=10, textvariable=self.dato)
    self.entry1.grid(column=1, row=0)
    
    self.label1 = tk.Label(self.ventana, text="Ingrese un numero 2: ")
    self.label1.grid(column=0, row=1)
    
    self.dato2 = tk.StringVar()
    self.entry2 = tk.Entry(self.ventana, width=10, textvariable=self.dato2)
    self.entry2.grid(column=1, row=1)
    
    self.boton = tk.Button(self.ventana, text="Calcular la suma", command=self.calcularSuma)
    self.boton.grid(column=0, row=2)
    
    self.labe2 = tk.Label(self.ventana, text="resultado")
    self.labe2.grid(column=1, row=2)

    self.ventana.mainloop()
    
  def calcularSuma(self):
    valor1 = int(self.dato.get())
    valor2 = int(self.dato2.get())
    suma = valor1 + valor2
    self.labe2.configure(text=suma)
    
aplicacion = Aplicacion()
    
    
