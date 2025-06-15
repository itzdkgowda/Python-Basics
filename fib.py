def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a


n=int(input("Enter a number: "))
print(fib(n))


# for i in range(10):
#     print(fib(i), end=" ")
