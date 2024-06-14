lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

for i in range(len(lista)):
  for j in range(len(lista[i])):
    if i == 0 and lista[i][j] > 50:
      lista[i][j] = 0
      print(lista[i][j])
    else: 
      print(lista[i][j])