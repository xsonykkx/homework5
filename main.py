immutable_var = (2, 4, 'hello', False)
print(immutable_var)
immutable_var [1] = 7   # нелья изменить значения элементов кортежа, так как кортеж не поддерживает обращение по элементам
print(immutable_var)
mutable_list = [1, 5, 'Sonya', True]
mutable_list[2] = 'Sofia'
print(mutable_list)