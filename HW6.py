# ; Задача 30: Заполните массив элементами арифметической
# ; прогрессии. Её первый элемент, разность и количество
# ; элементов нужно ввести с клавиатуры. Формула для
# ; получения n-го члена прогрессии: 
# ; Каждое число вводится с новой строки.

# x = int(input("Введите первый элемент массива А = "))
# N = int(input("Введите кол-во элементов массива А = "))
# d = int(input("Введите разность/шаг = "))
# for i in range(N):
#     print(x+i*d, end = " ")# программа идёт так 7 + 0*2=> 7; 7+1*2=>9 и до N

# из решения ГБ
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# from random import randint
 
# min, max = 5, 15
# #data = [randint(1, 10) for _ in range(20)]
# data=[-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# print("Original array:", data, sep='\n')
# indexes = [i for i, v in enumerate(data) if min <= v <= max]
# print("Indexes:", indexes, sep='\n')
# result = []
# i = len(indexes)
# while i :
#     i -= 1
#     result.append(data.pop(indexes[i]))#от всего списка отнимаются нужные элементы
# print("Остальные элементы:", data, sep='\n')
# print("Необходимые элементы:", result, sep='\n')


## из решения ГБ
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)
