#odds = [x for x in squares if x % 2 != 0 ]

paises = []
temperaturas = []
for i in range(3):
  pais = input("Ingrese un pais: ")
  paises.append(pais)
  temp1 = float(input("Ingrese la temperatura media 1: "))
  temp2 = float(input("Ingrese la temperatura media 2: "))
  temp3 = float(input("Ingrese la temperatura media 3: "))
  temperaturas.append([temp1, temp2, temp3])

print("Imprimir las listas")
for k in range(3):
  print(f"Pais: {paises[k]} => temperaturas: {temperaturas[k]}")

media_total = []
for j in range(3):
  media = (temperaturas[j][0] + temperaturas[j][1] + temperaturas[j][2]) / 3
  media_total.append(media)

print("Imprimir las listas")
for m in range(3):
  print(f"Pais: {paises[m]} => temperatura media: {media_total[m]}")


paisMayor = paises[0]
temperaturaMayor = media_total[0]
for x in range(1, 3):
   if temperaturaMayor < media_total[x]:
      temperaturaMayor = media_total[x]
      paisMayor = paises[x]

print(paisMayor, temperaturaMayor)
