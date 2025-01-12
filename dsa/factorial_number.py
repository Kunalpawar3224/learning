n = 7

k = 1

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
    for i in range(1, 8):
        k = k * i

print("k = ", k)

###########################################

# Second Implementaton
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        # print(x * factorial(x-1))
        return (x * factorial(x-1))


print("factorial = ",factorial(6))