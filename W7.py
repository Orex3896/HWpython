# кортежи
# a = (1, 2, 3, 4, 5, 6)
# print(a.__sizeof__())
# b = [1, 2, 3, 4, 5, 6]
# print(b.__sizeof__())
# c=tuple()
# c = 1,2,3 ,4 ,5
# print(c)
# print(c.__sizeof__())
# a = tuple('hello, world!')
# print(a)
#
# 
#  Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.

def func(li):
    dict = {i[0] * i[1]: i for i in li if i[0] != i[1]}

    return max(dict.items())[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]

print(*func(orbits))


# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для
# разных объектов отличается - то False.
# Для пустого набора объектов,
# функция должна возвращать True.
# Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print('same')
# else:
# print('different')
def same_by(characteristic, objects):
    #так же нужна проверка если список пустой
    return len(set(map(characteristic, objects))) == 1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')