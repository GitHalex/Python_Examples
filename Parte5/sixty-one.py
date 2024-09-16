import tkinter as tk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.TK()
    
    self.seleccion1 = tk.IntVar()
    self.check1 = tk.Checkbutton(self.ventana1, text="Python", variable=self.seleccion1)
    self.check1.grid(column=0, row=0)
    
    self.seleccion2 = tk.IntVar()
    self.check2 = tk.Checkbutton(self.ventana1, text="C++", variable=self.seleccion2)
    self.check2.grid(column=0, row=1)
    
    self.seleccion3 = tk.IntVar()
    self.check3 = tk.Checkbutton(self.ventana1, text="Java", variable=self.seleccion3)
    self.check3.grid(column=0, row=2)
    
    self.boton1 = tk.Button()
    
    
    self.ventana1.mainloop()