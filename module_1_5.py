immutable_var = 1, 2, "terminator", True
print(immutable_var)
print(type(immutable_var))
#immutable_var[1] = 100 - TypeError: 'tuple' object does not support item assignment
#print(immutable_var)
immutable_var_1 = [5, 17], ['dot']
print(immutable_var_1)
print(type(immutable_var_1))
immutable_var_1[1][0] = 'все нормально'
print(immutable_var_1)

mutable_list = [2024, 'сентябрь', 22.09, 'power']
print(mutable_list)
print(type(mutable_list))
mutable_list[0] = 'до нашей эры'
print(mutable_list)