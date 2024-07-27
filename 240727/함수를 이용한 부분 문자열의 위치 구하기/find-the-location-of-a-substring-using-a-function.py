def bubun_str(str1,str2):
    for i in range(len(str1)-len(str2)+1):
        if str2 == str1[i:i+len(str2)]:
            return i
    return -1

str1 = input()
str2 = input()
result = bubun_str(str1,str2)
print(result)