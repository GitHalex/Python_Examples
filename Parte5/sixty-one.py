import tkinter as tk 

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.seleccion1 = tk.IntVar()
    self.check1 = tk.Checkbutton(self.ventana1, text="Python", variable=self.seleccion1)
    self.check1.grid(column=0, row=0)
    
    self.seleccion2 = tk.IntVar()
    self.check2 = tk.Checkbutton(self.ventana1, text="C++", variable=self.seleccion2)
    self.check2.grid(column=0, row=1)
    
    self.seleccion3 = tk.IntVar()
    self.check3 = tk.Checkbutton(self.ventana1, text="Java", variable=self.seleccion3)
    self.check3.grid(column=0, row=2)
    
    self.boton1 = tk.Button(self.ventana1, text="Verificar", command=self.verificar)
    self.boton1.grid(column=0, row=4)
    
    self.label1 = tk.Label(self.ventana1, text="cantidad")
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
      
    self.label1.configure(text="cantidad:"+str(cant))
    
# aplicacion = Aplicacion()


class Aplicacion_One:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.seleccion = tk.IntVar()
    self.check1 = tk.Checkbutton(self.ventana1, text="¿Esta de acuerdo con los terminos y condiciones?", variable=self.seleccion, command=self.cambiarestado)
    self.check1.grid(column=0, row=0)
    
    self.boton1=tk.Button(self.ventana1, text="Entrar", state="disabled", command=self.ingresar)
    self.boton1.grid(column=0, row=1)
            
    self.ventana1.mainloop()
    
  def cambiarestado(self):
    if self.seleccion.get() == 1:
      self.boton1.configure(state="normal")
    if self.seleccion.get() == 0:
      self.boton1.configure(state="disabled")
      
  def ingresar(self):
    self.ventana1.title("Ingresando...")
    
# aplicaion_one = Aplicacion_One()

class Aplicacion_Nav:
  def __init__(self) -> None:
    self.ventana = tk.Tk()
    
    self.seleccion1 = tk.IntVar()
    self.check1 = tk.Checkbutton(self.ventana, text="Google Chrome", variable=self.seleccion1)
    self.check1.grid(column=0, row=0)
    
    self.seleccion2 = tk.IntVar()
    self.check2 = tk.Checkbutton(self.ventana, text="Microsoft Edge", variable=self.seleccion2)
    self.check2.grid(column=0, row=1)
    
    self.seleccion3 = tk.IntVar()
    self.check3 = tk.Checkbutton(self.ventana, text="Brave", variable=self.seleccion3)
    self.check3.grid(column=0, row=2)
    
    self.boton_uno = tk.Button(self.ventana, text="navegador", command=self.navegador)
    self.boton_uno.grid(column=0, row=3)
    
    self.ventana.mainloop()
    
  def navegador(self):
    if self.seleccion1.get() == 1: self.ventana.title("Google Chrome")
    if self.seleccion2.get() == 2: self.ventana.title("Microsoft Edge")
    if self.seleccion3.get() == 3: self.ventana.title("Brave")
    

    
navegador = Aplicacion_Nav()