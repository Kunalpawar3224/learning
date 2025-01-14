# a = [1, 2, 3, 4, 5]

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    print("digit = ", digit)
    reversed_num = reversed_num * 10 + digit
    print("reversed_num = ", reversed_num)
    num //= 10
    print("num = ",num)

print("Reversed Number: " + str(reversed_num))
# a.reverse()

# print(a)