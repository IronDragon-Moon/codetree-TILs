def is_sosu(n):
    for i in range(2,n):
        if n%i ==0: return False
    return True
def all_zzak(n):
    hap =0
    for i in range(len(str(n))):
        # if (n%10)%2 != 0:
        #     return False
        hap += n%10
        n = n//10
    if hap %2 == 0:
        return True
    else:
        return False
a,b = map(int,input().split())
cnt = 0
for i in range(a,b+1):
    if is_sosu(i) and all_zzak(i): cnt +=1 
print(cnt)