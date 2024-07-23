def has_369(n):
    str_n = str(n)
    for chr1 in str_n:
        if int(chr1) in (3,6,9):
            return True
    return False

def is_magic_num(n):
    return has_369(n) or n%3 ==0

a,b = map(int,input().split())
cnt =0
for i in range(a,b+1):
    if is_magic_num(i):
        cnt += 1
print(cnt)