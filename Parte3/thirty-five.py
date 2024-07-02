def cargarAlumos() -> None:

  alumnos = {}

  for i in range(1, 4):
    ci = str(i) + str(int(input("Ingrese su CI: ")))
    materia = input("Ingrese materia: ")
    nota = float(input("Ingrese su nota: "))
    alumnos[ci] = (materia, nota)
  
  return alumnos


def imprimir(alumnos: dict) -> None:
    print("Listado completo de alumnos:")
    for ci in alumnos:
        print(ci,alumnos[ci][0],alumnos[ci][1])


def consulta(alumnos):
    ci=str(int(input("Ingrese el codigo de articulo a consultar:")))
    if ci in alumnos:
        print(alumnos[ci][0])
    else:
        print(f"ci: {ci} no existe")
        

alumnos = cargarAlumos()
imprimir(alumnos)
consulta(alumnos)