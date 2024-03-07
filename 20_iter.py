for i in range(1, 11):
  print(i)

my_iter = iter(range(1, 11))
print(my_iter)

# Con el ITER podemos manjear iteraciones manualmente.
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Iteración manual = genera una excepción y tiene un límite.
# Cuando llega más allá del rango dado genera un error: StopIteration
