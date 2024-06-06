immutable_var = 1, 2, 'string', True
print(immutable_var)
immutable_var[2] = 'column'
print(immutable_var) # кортеж не поддержтвает изменение элементов внутри него

mutable_list = [4, 5, 'Hello']
mutable_list[2] = 'See you'
print(mutable_list) # чтобы эта команда запустилась, необходимо исправить ошибку выше.