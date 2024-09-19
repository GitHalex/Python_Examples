import tkinter as tk 

""" class Aplicacion:
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
    
    self.boton1 = tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
    self.boton1.grid(column=0, row=1)
    
    self.label1 = tk.Label(self.ventana1, text="Seleccionado")
    self.label1.grid(column=0, row=2)

    self.ventana1.mainloop()

  def recuperar(self):
    if len(self.listbox1.curselection()) != 0:
      self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))
    
aplicacion1 = Aplicacion() """


""" class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.listbox1 = tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE)
    self.listbox1.grid(column=0, row=0)
    self.listbox1.insert(0, "papa")
    self.listbox1.insert(1, "manzana")
    self.listbox1.insert(2, "pera")
    self.listbox1.insert(3, "sandia")
    self.listbox1.insert(4, "naranja")
    self.listbox1.insert(5, "melon")

    self.boton1 = tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
    self.boton1.grid(column=0, row=1)

    self.label1 = tk.Label(self.ventana1, text="Seleccionado:")
    self.label1.grid(column=0, row=2)
    self.ventana1.mainloop()

  def recuperar(self):
    if len(self.listbox1.curselection()) != 0:
      todas = ''
      for posicion in self.listbox1.curselection():
        todas += self.listbox1.get(posicion) + "\n"
      self.label1.configure(text=todas)

aplicacion = Aplicacion() """

""" class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()

    self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
    
    self.listbox1 = tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
    self.listbox1.grid(column=0, row=0)
    self.scroll1.configure(command=self.listbox1.yview)
    self.scroll1.grid(column=1, row=0, sticky='NS')
    self.listbox1.insert(0, "papa")
    self.listbox1.insert(1, "manzana")
    self.listbox1.insert(2, "pera")
    self.listbox1.insert(3, "sandia")
    self.listbox1.insert(4, "naranja")
    self.listbox1.insert(5, "melon")
    self.listbox1.insert(6, "limon")
    self.listbox1.insert(7,"kiwi")
    self.listbox1.insert(5,"banana")
    self.listbox1.insert(5,"uva")
    self.listbox1.insert(5,"papaya")
    self.listbox1.insert(5,"mandarina")
    self.listbox1.insert(5,"frutilla")
    
    self.boton1 = tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
    self.boton1.grid(column=0, row=1)
    
    self.label1 = tk.Label(self.ventana1, text="Seleccionado:")
    self.label1.grid(column=0, row=2)
    
    self.ventana1.mainloop()

  def recuperar(self):
    if len(self.listbox1.curselection()) != 0:
      todas = ""
      for posicion in self.listbox1.curselection():
        todas += self.listbox1.get(posicion) + "\n"

      self.label1.configure(text=todas)
      
aplicacion = Aplicacion() """

class Aplicacion:
  def __init__(self) -> None:
    self.ventana1 = tk.Tk()
    
    self.nombre = tk.StringVar()
    self.entry1 = tk.Entry(self.ventana1, width=20, textvariable=self.nombre)
    self.entry1.grid(column=0, row=0)

    self.listbox1 = tk.Listbox(self.ventana1)
    self.listbox1.grid(column=0, row=1)
    self.listbox1.insert(0, "Bolivia")
    self.listbox1.insert(1, "Peru")
    self.listbox1.insert(2, "Chile")
    self.listbox1.insert(3, "Brasil")
    
    self.boton1 = tk.Button(self.ventana1, text="Mostrar Dato", command=self.mostrar)
    self.boton1.grid(column=0, row=2)
    
    self.labelNombre = tk.Label(self.ventana1, text="Nombre")
    self.labelNombre.grid(column=0, row=3)

    self.labelPais = tk.Label(self.ventana1, text="Nacionalidad")
    self.labelPais.grid(column=1, row=3)
    
    self.ventana1.mainloop()
    
  def mostrar(self):
    self.labelNombre.configure(text=self.nombre.get())
    if len(self.listbox1.curselection()) != 0:
      self.labelPais.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))
      
aplicacion = Aplicacion()