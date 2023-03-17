# #задача№16
# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# list_1 = [int(i) for i in input("введите элементы массива =").split()]
# print(list_1)
# x= int(input("Введите число которое нужно найти = "))
# print(list_1.count(x))

#-------------------------------
# n = [1,2,3,5,6]
# k=4
# print(n.count(k))



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X


# import random
# A = [i for i in range(1,11)]
# i=0
# random.shuffle(A)
# print(A)
# x=int(input("Введите заданное число = "))
# #-----------
# #-----------
# while i in range(len(A)):
#     if A[i] !=x:
#         i+=1
#     else:
#         result = [A[i]-1, A[i]+1]
#         break
# else:
#     result=A[len(A)-1]

# print(result)

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква 
# имеет определенную ценность. В случае с английским алфавитом
# очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы
# оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М,
# П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц,
# Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова. Будем считать, что на вход подается только 
# одно слово, которое содержит либо только английские, либо только 
# русские буквы.

eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

D_Eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
D_Rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in eng:
    summa = 0
    for letter in word:
        for key, value in D_Eng.items():
            if letter.upper() in value:
                summa += key
    print(f'стоимость введенного английского слова = {summa}')
else:
    if word[0].lower() in rus:
        summa = 0
        for letter in word:

            for key, value in D_Rus.items():
                if letter.upper() in value:
                    summa += key
    print(f'стоимость введенного русского слова = {summa}')