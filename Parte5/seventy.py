import tkinter as tk
from tkinter import ttk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.agregar_menu()
    self.ventana1.mainloop()

  def agregar_menu(self):
    self.menubar1 = tk.Menu(self.ventana1)
    self.ventana1.config(menu=self.menubar1)

    self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
    self.opciones1.add_command(label="Configurar ventana", command=self.configurar)
    self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)

  def configurar(self):
    dialogo1 = DialogoTamano(self.ventana1)
    s = dialogo1.mostrar()
    self.ventana1.geometry(s[0]+"x"+s[1])

class DialogoTamano:
  def __init__(self) -> None:
    pass
    
