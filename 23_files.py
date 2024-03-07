file = open('./text.txt')
# print(file.read()) # Leer el archivo completo

#print(file.readline()) # Leer línea por línea
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
  print(line)

file.close()  # Se cierra para liberar memoria en Python

# Con With cerramos automáticamente al finalizar el bloque
with open('./text.txt') as file:
  for line in file:
    print(line)
