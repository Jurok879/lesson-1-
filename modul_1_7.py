grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]   # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                         # множество

my_grades = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
             sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
             sum(grades[4])/len(grades[4])]                                 # находим среднюю оценку каждого студента

my_students = sorted(students)                                              # сортируем имена по алфавиту

my_dict = dict(zip(my_students, my_grades))                                 # составляем словарь
print(my_dict)