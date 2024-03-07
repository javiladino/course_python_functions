# Creando un conjunto -- Atención : No es un diccionario.
set_countries = {'Col', 'Mex', 'Bol'}
print(set_countries)
print(type(set_countries))

# Elimina los elementos duplicados que metamos en el conjunto

set_countries.add('Arg')
print(set_countries)

set_numbers = {1,2,2,443,23}
print(set_numbers)

set_types = {1,'hola', False, 12.12}
print(set_types)

set_from_strings = set('hola')
print(set_from_strings)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers= [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
