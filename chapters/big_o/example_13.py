counter = 0
def fib(n):
    global counter
    counter +=1

    print(f'call number: {counter}')

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


fib(20)
