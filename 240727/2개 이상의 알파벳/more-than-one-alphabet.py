def is_diffAlpha(s):
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            return True
    return False

str1 = input()
if is_diffAlpha(str1):
    print("Yes")
else:
    print("No")