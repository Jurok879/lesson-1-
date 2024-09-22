my_dict = {'Сергей': 1973, 'Иван': 1985, 'Эдик': 2001, 'Виктор': 1994 }    # словарь
print(my_dict)
print(my_dict['Эдик'])                                                     # одно значение по ключу
print(my_dict.get('Ольга'))                                                # не существующий ключ
my_dict.update({'Вадик': 2005,
                'Евгений': 1979})                                          # добавлено две пары в словарь
print(my_dict)
a = my_dict.pop('Эдик')                                                    # удалена пара по ключу и выведено значение
print(a)
print(my_dict)                                                             # словарь

my_set = {1, 1, 4, 5, 5, 8, 9, True, False, 0, 'water'}                    # множество
print(my_set)
my_set.add(2)                                                              # добавили один элемент
my_set.add(3)                                                              # добавили второй элемент
my_set.discard(False)                                                      # удалили элемент
print(my_set)
