n,m =map(int,input().split())
list_ = list(map(int,input().split()))
def fun():
    global m
    result = 0
    if m==1:
        return list_[0]
    while True:
        result += list_[m-1]
        if m%2==1:
            m -= 1
        elif m%2==0:
            m //= 2
        if m==1:
            result += list_[m-1]
            return result
print(fun())