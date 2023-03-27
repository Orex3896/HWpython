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

# list_1 = []
# for i in input():
#     list_1.append(i)
# print(list_1)
# num_min=int("Введите минимальное значение списка = "+input())
# num_max=int("Введите максимальное значение списка = "+input())
# for ind in ind:
#     if num_min<=val<=num_max:
#         val in enumerate(list_1)
# print(list_1)

from random import randint
 
lo, hi = 5, 15
#data = [randint(1, 10) for _ in range(20)]
data=[-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
print("Original array:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Indexes:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Remaining elements:", data, sep='\n')
print("Required elements:", result, sep='\n')