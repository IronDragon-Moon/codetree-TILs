n = int(input())
def ascend(n):
    if n==0:
        return
    ascend(n-1)
    print(n,end=' ')
def descend(n):
    if n==0:
        return
    print(n,end=' ')
    descend(n-1)
ascend(n)
print()
descend(n)