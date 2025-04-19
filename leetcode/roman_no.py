class Solution:
    def romanToInt(self, s: str) -> int:
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000

        a = list(s)
        # print("a = ", a)
        g = 0
        n = len(a)
        for w in range(0, n):
            # print(w)
            if a[w] == "I":
                g = I + g
            if a[w] == "V":
                if a[w-1] == "I":
                    g = V-I-1 + g
                    print("g6 = ", g)
                else:
                    g = V + g
                    print("g5 = ", g)
            if a[w] == "X":
                if a[w-1] == "I":
                    g = X-I-1 + g
                elif a[w+1] == "C" or "L":
                    None
                else:
                    g = X+ g
            if a[w] == "L":
                if a[w-1] == "X":
                    g = L-X + g
                else:
                    g = L + g
            if a[w] == "C":
                if a[w-1] == "X":
                    g = C-X + g
                    print("g4 = ", g)
                elif a[w+1] == "M" or "D":
                    None
                else:
                    g = C + g
                    print("g3 = ", g)
            if a[w] == "D":
                if a[w-1] == "C":
                    g = D-C + g
                else:
                    g = D + g
            if a[w] == "M":
                if a[w-1] == "C":
                    g = M-C + g
                    print("g2 = ", g)
                else:
                    g = M + g
                print("g1 = ", g)
        print(type(I))
        print(g)


sol = Solution()
sol.romanToInt("MCMXCIV")

