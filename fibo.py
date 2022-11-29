# Fibonacci numbers module

def fibo(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

series=fibo(2000)
if __name__=='_main_':
 print(series)