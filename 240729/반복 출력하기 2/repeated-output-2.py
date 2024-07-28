n = int(input())
def say_hello(n):
    if n==0:
        return
    say_hello(n-1)
    print("HelloWorld")

say_hello(n)