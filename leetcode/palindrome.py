class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_list = [x1 for x1 in str(x)]
        # n = len(x_list)
        # for i in range (0, n):
        #     # for j in range(i+1):
        #         # if isinstance(x_list[i], int):
        #     if not x_list[0]:
        #             p = p + int(x_list[i])
        #         p = int(x_list[i]) * 10
        #         print(p)
        #         print("x_list+1", x_list[1]) 
        #     else:
        #         p =  x_list[i]
        # print('p, x = ', p, x)
        # if p == x:
        #     return true
        # else:
        #     return False

        palindrom = False
        x = str(x)

        if "-" in x:
            palindrom = False
        if not '-' in x:
            s = x.lower().replace(" ", "")
            s = s[::-1]
            s = int(s)
            print("x, s = ", x, s)
            x = int(x)
            if x == s:
                palindrom = True
        
        return palindrom

        
        