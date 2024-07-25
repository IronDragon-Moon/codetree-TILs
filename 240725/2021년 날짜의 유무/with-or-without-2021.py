def has_date(M,D):
    if M in [1,3,5,7,8,10,12]:
        if D<=31: return True
    elif M in [4,6,9,11]:
        if D<=30: return True
    elif M==2 and D<=28:
        return True
    return False

M,D = map(int,input().split())
if has_date(M,D):
    print("Yes")
else:
    print("No")