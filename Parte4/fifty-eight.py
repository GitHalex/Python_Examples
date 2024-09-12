""" import tkinter as tk

class Aplicacion:
  def __init__(self) -> None:
    self.valor = 1
    self.ventana1 = tk.Tk()
    self.ventana1.title("Controles Button y Label")
    self.label1 = tk.Label(self.ventana1, text=self.valor)
    self.label1.grid(column=2, row=0)
    self.label1.configure(foreground="blue")
    
    self.boton1 = tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
    self.boton1.grid(column=1, row=0)
    
    self.boton2 = tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
    self.boton2.grid(column=3, row=0)
    
    self.ventana1.mainloop()

    
  def incrementar(self):
      self.valor = self.valor + 1
      self.label1.config(text=self.valor)
      
  def decrementar(self):
      self.valor = self.valor - 1
      self.label1.config(text=self.valor)
      
      
aplicacion = Aplicacion() """

""" import tkinter as tk 
import sys

class Aplicacion:
  
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.ventana1.title("Prueba")
    self.label1 = tk.Label(self.ventana1, text="Sistema de facturacion")
    self.label1.grid(column=0, row=0)
    self.label2 = tk.Label(self.ventana1, text="2018")
    self.label2.grid(column=0, row=1)
    self.boton1 = tk.Button(self.ventana1, text="Finalizar", command=self.finalizar)
    self.boton1.grid(column=0, row=2)
    self.ventana1.resizable(False, False)
    self.ventana1.mainloop()

  def finalizar(self):
    sys.exit(0)
    

aplicacion = Aplicacion() """

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Seleccione la cantidad de bultos:")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.spinbox1=ttk.Spinbox(self.ventana1, from_=0, to=100, width=10, state='readonly')        
        self.spinbox1.set(0)        
        self.spinbox1.grid(column=1, row=0, padx=10, pady=10)
        self.boton1=ttk.Button(self.ventana1, text="Sortear", command=self.sortear)
        self.boton1.grid(column=0, row=1, padx=10, pady=10)
        self.label2=ttk.Label(self.ventana1, text="", width=20)
        self.label2.grid(column=1, row=1, padx=10, pady=10)
        self.ventana1.mainloop()

    def sortear(self):
        if int(self.spinbox1.get())==0:
            mb.showerror("Cuidado","Debe seleccionar un valor distinto a cero en bultos")
        else:
            valor=random.randint(1,3)
            if valor==1:
                self.label2.configure(text="Se deben revisar")
                self.label2.configure(background="red")
            else:
                self.label2.configure(text="No se revisan")
                self.label2.configure(background="green")

aplicacion1=Aplicacion() 
    

    