def message_creator(text):
  # Escribe tu solución 👇
  respuestas = {
      'computadora': "Con mi computadora puedo programar usando Python",
      'celular': "En mi celular puedo aprender usando la app de Platzi",
      'cable': "¡Hay un cable en mi bota!"
  }

  if text in respuestas.keys():
    return respuestas[text]
  else:
    return 'Artículo no encontrado'


text = 'computadora'
response = message_creator(text)
print(response)



# Segunda forma de solucionarlo
def message_creator2(text):
  if text == 'computadora':
    return 'Con mi computadora puedo programar usando Python'
  elif text == 'celular':
    return 'En mi celular puedo aprender usando la app de Platzi'
  elif text == 'cable':
    return '¡Hay un cable en mi bota!'
  else:
    return 'Artículo no encontrado'


response = message_creator2('celular')
print(response)
