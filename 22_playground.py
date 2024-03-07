
# Solución 1: en una línea con Lambda y MAP
"""
numbers = [1, 2, 3, 4]
result = list(map(lambda number: number * 2, numbers))
print(result)
"""

# Solución 2: con una variable DEF
def multiply_numbers(numbers):
  # Escribe tu solución 👇
  result = list(map(lambda number: number * 2, numbers))
  return (result)

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
