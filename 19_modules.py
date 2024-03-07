import sys # Importamos el módulo sys con información del sistema donde se ejecuta el archivo
print(sys.path)

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
#Esta expresión regular busca lo indicado dentro de [ ] 
print(result)

import time
timestamp = time.time() 
#hora actual en formato de computadora
print(timestamp) 
local = time.localtime()
#Indica la hora local
result = time.asctime(local) 
#Transforma el formato de hora
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
#Devuelve un diccionario con el número de veces que se repite un item dentro de un elemento (frecuencia)
print(counter)
