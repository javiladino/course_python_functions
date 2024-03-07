'''
numbers = []
for element in range(1,11):
  numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2 )
'''

numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)

days = [
    "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"
]

newlist = [i for i in days if "a" in i]

print(newlist)

numeros = [35, 16, 10, 34, 37, 25]

numeros_2 = [num for num in numeros if num % 2 == 0]
print (numeros_2)

numeros_3 = [num for num in numeros if num % 2 != 0]

print (numeros_3)

numeros_4 = [num * 2 for num in numeros]
print(numeros_4 )

nombres = ["david", "maria", "juan", "pedro", "ana", "luis"]
nom_use = [nom.upper() for nom in nombres if len(nom) >= 5]
print(nom_use)

nom_use_2 = [nom for nom in nombres if len(nom) < 5 if nom[0] == "a"]
print(nom_use_2)

nom_use_3 = [nom for nom in nombres if "a" in nom]
print(nom_use_3)