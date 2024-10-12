import tkinter as tk 
from tkinter import ttk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.crear_botones()
    
    self.canvas1 = tk.Canvas(self.ventana1, width=600, height=400, background="black")
    self.canvas1.grid(column=0, row=1)
    
    self.linea = self.canvas1.create_line(0, 0, 100, 50, fill="white")
    self.rectangulo = self.canvas1.create_rectangle(150, 10, 300, 110, fill="white")
    self.ovalo = self.canvas1.create_oval(400, 10, 500, 150, fill="red")

    self.canvas1.create_rectangle(100, 300, 150, 350, fill="#aaaaaa", tags="cuadrado")
    self.canvas1.create_rectangle(200, 300, 250, 350, fill="#555555", tags="cuadrado")
    self.canvas1.create_rectangle(300, 300, 350, 350, fill="#cccccc", tags="cuadrado")

    self.ventana1.mainloop()

  def crear_botones(self):
    

