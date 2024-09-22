immutable_var = (8, 'kolos', True, 1+4j)       # кортеж из разных типов данных
print(immutable_var)
# immutable_var[1]='tea'                       # замена элемента кортежа
print(immutable_var)                           # ошибка, т.к. кортеж не меняет элементы внутри списка

mutable_list = [7, 'baii', False, 1+3j]        # список из нескольких элементов
print(mutable_list)
mutable_list[1] = 'cube'                       # замена элемента
print(mutable_list)