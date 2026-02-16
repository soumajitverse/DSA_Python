n = int(input("Enter n: "))

def fib(n):
    if(n == 1):
        return 0
    if(n == 2 or n == 3):
        return 1
    return fib(n-1) + fib(n-2)
    
print("nth fibonacci no. is: ", fib(n))