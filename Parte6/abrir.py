arch1 = open("datos.txt", "a")
arch1.write("nueva linea de otra 1\n")
arch1.write("nueva linea de otra 2\n")
arch1.close()

arch1 = open("datos.txt","r")
contenido = arch1.read()
print(contenido)
arch1.close()