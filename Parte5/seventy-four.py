""" import tkinter as tk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()

    self.canvas1 = tk.Canvas(self.ventana1, width=600, height=400, background="black")
    self.canvas1.bind("<Motion>", self.mover_mouse)
    self.canvas1.bind("<Button-1>", self.presion_mouse)
    self.canvas1.grid(column=0, row=1)
    self.ventana1.mainloop()

  def presion_mouse(self, evento):
    self.canvas1.create_oval(evento.x-5, evento.y-5, evento.x+5, evento.y+5, fill="red")

  def mover_mouse(self, evento):
    self.ventana1.title(str(evento.x)+"-"+str(evento.y))

aplicacion = Aplicacion() """


import tkinter as tk 

class Aplicacion:
  
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    self.canvas1 = tk.Canvas(self.ventana1, width=600, height=400, background="black")
    self.canvas1.grid(column=0, row=0)
    self.canvas1.bind("<ButtonPress-1>", self.boton_presion)
    self.canvas1.bind("<Motion>", self.mover_mouse)
    self.canvas1.bind("<ButtonRelease-1>", self.boton_soltar)
    self.presionado = False
    self.ventana1.mainloop()

  def boton_presion(self, evento):
    self.presionado = True
    self.origenx = evento.x
    self.origeny = evento.y

  def mover_mouse(self, evento):
    if self.presionado:
      self.canvas1.create_line(self.origenx, self.origeny, evento.x, evento.y, fill="red")
      self.origenx = evento.x
      self.origeny = evento.y

  def boton_soltar(self, evento):
    self.presionado = False

aplicacion = Aplicacion()