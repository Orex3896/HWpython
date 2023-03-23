

def ex(b, n):
    if n==0:
        return 1
    return b*ex(b, n-1)
b = int(input("b = "))
n = int(input("n = "))
print(ex(b,n))