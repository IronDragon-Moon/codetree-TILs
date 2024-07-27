def abs_list(arr):
    for i in range(len(arr)):
        arr[i]= abs(arr[i])

n = int(input())
list_ = list(map(int,input().split()))
abs_list(list_)
for i in list_:
    print(i,end=' ')