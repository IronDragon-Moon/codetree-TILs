def is_palin(str2):
    if str2 == str2[::-1]:
        return True
    else:
        return False

str1 = input()
if(is_palin(str1)):
    print("Yes")
else:
    print("No")