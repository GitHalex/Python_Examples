""" def empleados() -> list:
    empleadosLista = []
    for i in range(3):
        name = input("Ingrese su nombre: ")
        sueldo1 = int(input("primer Sueldo: "))
        sueldo2 = int(input("segundo Sueldo: "))
        sueldo3 = int(input("tercer Sueldo: "))
        empleadosLista.append([name, (sueldo1, sueldo2, sueldo3)])

    return empleadosLista

def sumaSueldos(listaEmpledos: list) -> None:
    
    for empleado in listaEmpledos:
        name = empleado[0]
        sueldos = empleado[1]
        sumaSueldosTotal = sum(sueldos)
        print(f"Name: {name} => sueldo total: {sumaSueldosTotal}")

def sueldosMayores(listaSueldos: list) -> None:
    
    for chalan in listaSueldos:
        name = chalan[0]
        sueldoChalan = chalan[1]
        totalSueldos = sum(sueldoChalan)
        if totalSueldos > 10000:
            print(f"{name} => {totalSueldos}")

empleadolista = empleados()
sumaSueldos(empleadolista)
sueldosMayores(empleadolista) """


def addCandidatos() -> list:
    
    listaRes = []

    for i in range(3):
        candidato = input("ingrese un nombre: ")
        votosProvincia = [(input("ingrese la provincia: "), int(input("Ingrese los votos: "))) for _ in range(1)]
        listaRes.append((candidato, votosProvincia))
      
    return listaRes

def imprimirVotos(candidatos: list) -> None:
    
    for candidato in candidatos:
        nombre = candidato[0]
        votosProvincia = candidato[1]
        for provincia, votos in votosProvincia:
            print(f"{nombre} => provincia: {provincia}, votos: {votos}")

candidatos = addCandidatos()
print(imprimirVotos(candidatos))



        

""" def cargar_paisespoblacion():
    paises=[]
    for x in range(5):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises


def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])


def pais_maspoblacion(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Pais con mayor cantidad de habitantes:",paises[pos][0])
    

# bloque principal

paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises) """