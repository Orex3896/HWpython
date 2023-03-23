# #ДЗ 1 задача реализация преподователя
# # n= input("n =").split()
# # m= input("m =").split()
# # first = [int(i) for i in input("first =").split()]#Ввод через пробел

# # second = [int(j) for j in input("second =").split()]

# # print(*sorted(set(first).intersection(second)))

# # #Задача №2

# # n = int(input())
# # bushes = [int(i) for i in input().split()]
# # bush_max = 0

# # for i in range(n):
# #     bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1 if i < n - 1 else 0]
# #     if bush_sum > bush_max:
# #             bush_max = bush_sum

# # print(bush_max)

# # # ----------------------------------

# # n = int(input())
# # bushes = [int(i) for i in input().split()]
# # bush_max = 0

# # for i in range(-1, n - 1):
# #     bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
# #     if bush_sum > bush_max:
# #             bush_max = bush_sum

# # print(bush_max)

# # 4
# # 4 1 2 3
# # 4 2 1 3

# # Фибоначчи

# # Последовательностью Фибоначчи называется
# # последовательность чисел a0, a1, ..., an, ...,
# # где # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# # Требуется найти N-е число Фибоначчи
# # def sum_fib(a):
# #       if a in [0,1]:
# #         return 1
# #       return sum_fib(a-2)+sum_fib(a-1)
# # print(sum_fib(int(input("Введите до какого числа последовательность Фибоначи = "))))

# #задача №33
# import random
# n = int(input("Введите кол-во оценок = "))
# list_1=[random.randint(1,5) for i in range(n)]

# print(list_1)

# n_min=min(list_1)
# n_max=max(list_1)
# num = [n_min if i == n_max else i for i in list_1]
# print(num)

n = input()
b = input()
c = input()
print(n, b, c, sep='*')