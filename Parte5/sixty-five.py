import tkinter as tk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    menubar1 = tk.Menu(self.ventana1)
    
    self.ventana1.config(menu=menubar1)

    opciones1 = tk.Menu(menubar1)
    opciones1.add_command(label="Rojo")