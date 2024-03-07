set_countries = {'Col', 'Mex', 'Bol'}

size = len(set_countries)
print(size)

print('Col' in set_countries)
print('Arg' in set_countries)

# Add
set_countries.add('Arg')
print(set_countries)

#Update
set_countries.update({'Arg', 'Ecu', 'Per'})
print(set_countries)

#Remove
set_countries.remove('Col')
print(set_countries)
set_countries.remove('Arg')
print(set_countries)

#clear.. eliminar todo
set_countries.clear()
print(set_countries)

size = len(set_countries)
print(size)
