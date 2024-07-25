def is_bubun(A,B,n1,n2):
    end = n2
    for i in range(n1-n2+1):
        if A[i:end] == B: return True
        end += 1
    return False

n1,n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if is_bubun(A,B,n1,n2):
    print("Yes")
else: 
    print("No")