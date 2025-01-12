a, b = 0, 1

fib = []
for i in range(2, 15):
    k = a+b

    fib.append(k)
    a = b
    b = k

print(fib)

