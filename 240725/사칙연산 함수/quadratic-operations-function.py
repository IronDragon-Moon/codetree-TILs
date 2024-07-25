def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def gop(a,b):
    return a*b
def nanugi(a,b):
    return a//b
a,yun,b = input().split()
a = int(a)
b = int(b)
if yun =='+':
    print(f"{a} + {b} = {plus(a,b)}")
elif yun =='-':
    print(f"{a} - {b} = {minus(a,b)}")
elif yun == '*':
    print(f"{a} * {b} = {gop(a,b)}")
elif yun == '/':
    print(f"{a} / {b} = {nanugi(a,b)}")