install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup
import csv

# URL del sitio web
url = 'https://vandal.elespanol.com/guias/guia-the-legend-of-zelda-tears-of-the-kingdom-trucos-consejos-y-secretos/misiones-secundarias'

# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
  # Parsear el contenido HTML
  soup = BeautifulSoup(response.text, 'html.parser')

  # Encontrar la lista <ul> por su clase, ID u otro selectorython 
  ul_list = soup.find('ul', class_='example-list')

  # Verificar si se encontró la lista <ul>
  if ul_list:
    # Crear un archivo CSV
    with open('lista.csv', 'w', newline='') as csvfile:
      # Crear un objeto escritor CSV
      csv_writer = csv.writer(csvfile)

      # Iterar sobre los elementos de la lista <ul> y escribirlos en el archivo CSV
      for li in ul_list.find_all('li'):
        csv_writer.writerow([li.text.strip()])

    print("Lista extraída y guardada en lista.csv")
  else:
    print("No se encontró una lista <ul> en el sitio web.")
else:
  print("La solicitud GET no fue exitosa.")
