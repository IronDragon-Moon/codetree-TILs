def is_yoon(n):
    if n%4 ==0:
        if n%100 ==0 and n%400!=0:
            return False
        return True
    return False

y = int(input())
if is_yoon(y):
    print("true")
else:
    print("false")