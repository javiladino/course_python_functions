def sum_with_range(min, max): # Definimos la función
  sum = 0 # Inicializamos la variable sum
  for x in range(min, max): # Creamos un bucle for
    sum += x # Vamos sumando los valores de x
  return sum #

result = sum_with_range(10, 20) # Llamamos a la función y la guardamos como result
print(result) # Imprimimos el resultado