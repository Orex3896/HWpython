#print(int(input()) + int(input()) + int(input()))
#print(sum(int(input()) for _ in range(3)))
# put your python code here

# x = int(input())
# print (f'Следующее за числом {x} число: {x + 1}\nДля числа {x} предыдущее число: {x-1}')


# x = int(input())
# c = int(input())
# v = int(input()) 
# print((x+c*(v-1)))

# #geometric progress
# x = int(input())
# c = int(input())
# v = int(input()) 
# print((x*c**(v-1)))

# #size meter in santimeter
# x = int(input())#sm

# print(x//100)
# #print(int(input()) // 100)

# x = int(input("кол-во школьников = "))#школьники
# n = int(input("кол-во мандарин = "))#mandarini
# print(n//x)#скольким досталось мандарин 
# print(n%x)#остаток мандарин

# x = int(input())
# print(x//2+x%2)

# #определение места в вагоне из 9 купе
# x = int(input())
# print((x+3)//4)

# num = int(input())
# digit3 = num % 10
# print(digit3)
# digit2 = (num // 10) % 10
# print(digit2)
# digit1 = num // 100
# print(digit1)
# print(digit1, digit2, digit3, sep=',')



# num=(int(input()))
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print("Сумма цифр =",digit1+digit2+digit3)
# print("Произведение цифр =",digit1*digit2*digit3)


#задача №2
# a, b, c = map(int, input())#запятая обязательно
# print("Сумма цифр =", a + b + c)
# print("Произведение цифр =", c * b * a)

# a, b, c = input()

# print('Сумма цифр =', int(a) + int(b) + int(c))
# print('Произведение цифр =', int(a) * int(b) * int(c))

# num=(int(input()))
# c = num % 10
# b = (num // 10) % 10    
# a = num // 100
# print(a,b,c,sep="")
# print(a,c,b,sep="")
# print(b,a,c,sep="")
# print(b,c,a,sep="")
# print(c,a,b,sep="")
# print(c,b,a,sep="")
# #2var
# a,b,c = input()
# print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')

#3var!!!!!!!!!!!!!!!!!!!!!!!top
# n = list(input())

# for x in range( len(n)):
# 	for y in range( len(n)):
# 		for z in range( len(n)):
# 			for a in range( len(n)):
# 			    if x != y and x != z and z != y and x != a:
# 				    print(n[x] + n[y] + n[z]+ n[a])

# a,b,c,d = input()
# print("Цифра в позиции тысяч равна",a)
# print("Цифра в позиции сотен равна",b)
# print("Цифра в позиции десятков равна",c)
# print("Цифра в позиции единиц равна",d)
# #var #2
# a = input()
# b = ['тысяч', 'сотен', 'десятков', 'единиц']
# for i in range(4):
#     print('Цифра в позиции ' + b[i] + ' равна ' + a[i])

# #var #3
# a,b,c,d=input()
# print('Цифра в позиции тысяч равна '+a,'Цифра в позиции сотен равна '+b,'Цифра в позиции десятков равна '+c,'Цифра в позиции единиц равна '+d, sep='\n')

# x = int(input())
# a = x // 10000  
# print(a)                
# b = x % 10000 // 1000 #откусывает 1 число и делит на 1000 получаем 2 число
# print(b)           
# c = x % 1000 // 100     
# print(c)   
# d = x % 100 // 10    
# print(d)         
# e = x % 10  
# print(e) 

# print(x%10000)


# a='*'
# print(a*17)
# print(a+" "*15+a)
# print(a+" "*15+a)
# print(a*17)

# print('*' * 17)
# print('*', '*', sep=' ' * 15)
# print('*', '*', sep=' ' * 15)
# print('*' * 17)

# a=int(input())
# b=int(input())
# print('Квадрат суммы',a,'и',b,'равен',(a+b)**2)
# print('Сумма квадратов',a,'и',b,'равна',(a**2+b**2))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a**b+c**d)
# n = int(input())
# print(n, '+', n * 11, '+', n * 111, '=', n * 123)


#IF ELSE


# str1=str(input())
# str2=str(input())
# if str1==str2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
#     #var2
# print('Пароль принят' if input() == input() else 'Пароль не принят')

# num = int(input())
# if num%2==0:
#     print("Чётное")
# else:
#     print("Нечётное")
# print("Чётное" if num%2==0 else "Нечётное")

# 1+4 = 2-3

# num= int(input())
# a=num//1000
# b=num//100%10
# c=num%100//10
# d=num%10
# print("Да" if a+d==b-c else "Нет")

# age = int(input())
# print("Доступ разрешен" if age>=18 else "Доступ запрещен")

# a= int(input())
# b= int(input())
# c= int(input())
# b_a=b-a
# print("YES" if c==b_a + b else "NO")

# #нахождение минимального числа из 4
# a= int(input())
# b= int(input())
# c= int(input())
# d= int(input())
# X1=0
# X2=0
# if a<b:
#     X1=a
# else:
#     X1=b
# if c<d:
#     X2=c
# else:
#     X2=d
# print(X1 if X1<X2 else X2)

#Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

# age= int(input())
# if age<=13:
#     print("детство")
# if 14<=age<=24:
#     print("молодость")
# if 25<=age<=59:
#     print("зрелость")
# if age>=60:
#     print("старость")

# #2var
# n = int(input())
# print("старость" if n>59 else "зрелость" if n>24 else "молодость" if n>13 else "детство")

a= int(input())
b= int(input())
c= int(input())
sum=0
if a>0:
    sum+=a
if b>0:
    sum+=b
if c>0:
    sum+=c
print(sum)
    
