my_dict = {'Андрей': 1996, 'Никита': 1991, 'Светлана': 1990}
print(my_dict)
print(my_dict['Андрей'])
my_dict.get('Marat')
print(my_dict.get('Marat'))
my_dict.update({'Svetlana': 1999, 'Roman': 1995})
print(my_dict)
a = my_dict.pop('Никита')
print(my_dict)
print(a)

my_set = {2012, 'harman', (40, 45, 32)}
print(my_set)
print(my_set.add(2010))
print(my_set.add('apple'))
print(my_set)
print(my_set.remove(2012))
print(my_set)