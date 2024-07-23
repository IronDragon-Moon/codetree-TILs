a,b = map(int,input().split())
result = 0
def is_sosu(n):
    if n==1:
        return True
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

for i in range(a,b+1):
    if is_sosu(i):
        result+=i
print(result)