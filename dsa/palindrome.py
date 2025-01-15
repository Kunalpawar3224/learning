# str = 'JaVaJ'  
# strstr = str.casefold()  
# print("strstr = ", strstr)
# # This string is reverse.  
# rev = reversed(str)  
  
# if list(str) == list(rev):  
#    print("PALINDROME !")  
# else:  
#    print("NOT PALINDROME !")  

num = 121
temp = num  
rev = 0  
while(num > 0):  
    dig = num % 10  
    revrev = rev * 10 + dig  
    numnum = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  