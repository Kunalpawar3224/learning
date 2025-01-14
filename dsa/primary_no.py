n = 99
flag = False

for i in range(2, n):
    # print(i)
    if (n % i) == 0:

        flag = True
        break
    
if flag == True:
    print("It is not a primary no = ", n)
else:
    print("It is a primary no = ", n)





# print("123")