num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

promedio = (num1 + num2 + num3) / 3
print('The average of the three numbers is: %.2f' % promedio)

if promedio > 6:
  print('Aprobaste')
else:
  print('Reprobaste')
