n,m = map(int,input().split())
list_ =[0]+ list(map(int,input().split()))
def froma1_toa2(a,b):
    result =0
    for i in range(a,b+1):
        result += list_[i]
    return result

for i in range(m):
    a,b = map(int,input().split())
    print(froma1_toa2(a,b))