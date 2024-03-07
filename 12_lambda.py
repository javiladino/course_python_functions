# Crear una función def que incremente x en 1
def increment(x):
  return x + 1

result = increment(12)
print(result)

#Podemos asignar una función Lambda a una variable
increment_v2 = lambda x: x + 1

result = increment_v2(22)
print(result)

# Utilizamos f'' para hacer retornar un string -- Con .title trae el string en mayúscula
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('martina', 'ladino')
print(text)
