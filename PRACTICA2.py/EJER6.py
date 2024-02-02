def fibonacci(n):
    fib_num = [0, 1]
    while fib_num[-1] + fib_num[-2] <= n:
        fib_num.append(fib_num[-1] + fib_num[-2])
    return fib_num
fib_num = fibonacci(50)
print(fib_num)