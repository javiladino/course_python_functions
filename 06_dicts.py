import random

countries = ['col', 'mex', 'bol', 'pe']

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 50}
print(result)

text = 'Hola, soy Martina'
# Generar un diccionario a partir de las volaces del texto TEXT
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)


unique2 = {c: text.count(c) for c in text if c in 'aeiou'}
print(unique2)

# Playground 9/44
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

even_numbers_v2 = [number for number in numbers if number % 2 == 0]
print('v2 =>', even_numbers_v2)