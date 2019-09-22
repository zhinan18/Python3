a = int(input())
b = int(input())
c = int(input())



def masterFun(a,  b,  c):
    if a <= b and b <= c:
        print(a,b,c)
    elif b <= c and b <= a:
        print(b,c,a)
    elif c <= a and a <= b:
        print(c,a,b)
    elif a <= c and c <= b:
        print(a,c,b)
    elif b <= a and a <= c:
        print(b,a,c)
    else:
        print(c,b,a)


masterFun(a, b, c)

