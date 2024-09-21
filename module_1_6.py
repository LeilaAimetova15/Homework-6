#dictionary
my_dict = {'Masha' : 1997 , 'Sasha' : 2001 , 'Pasha' : 1990 }
print(my_dict)
print(my_dict['Pasha'])
print(my_dict.get('Misha'))
my_dict.update({'Misha' : 2005 , 'Petya' : 2013})
a=my_dict.pop('Sasha')
print(a)
print(my_dict)
#sets
my_set = {2, 4, 6, 2, 4, 'Name'}
print(my_set)
my_set.update({38, 'Year'})
my_set.discard(4)
print(my_set)