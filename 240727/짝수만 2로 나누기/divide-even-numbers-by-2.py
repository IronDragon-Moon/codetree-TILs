def change(arr):
    for i in range(len(arr)):
        if arr[i]%2 ==0:
            arr[i] //= 2


N = int(input())
list_ = list(map(int,input().split()))
change(list_)
for i in list_:
    print(i,end=' ')