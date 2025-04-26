class Solution:
    def romanToInt(self, s: str) -> int:
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000

        a = list(s)
        g = 0
        n = len(a)
        for w in range(0, n):
            if a[w] == "I":
                g = I + g
            if a[w] == "V":
                if a[w-1] == "I":
                    g = V-I-1 + g
                else:
                    g = V + g
            if a[w] == "X":
                if a[w-1] == "I":
                    g = X-I-1 + g
                elif a[w+1] == "C" or a[w+1] == "L":
                    None
                else:
                    g = X+ g
            if a[w] == "L":
                if a[w-1] == "X":
                    g = L-X + g
                else:
                    g = L + g
            if a[w] == "C":
                print("a")
                if a[w-1] == "X":
                    print("b")
                    g = C-X + g
                elif a[w+1] == "M" or a[w+1] == "D":
                    print(a[w+1] == "M" or "D")
                    print("c")
                    None
                else:
                    print("d")
                    g = C + g
                    print(g)
            if a[w] == "D":
                if a[w-1] == "C":
                    g = D-C + g
                else:
                    g = D + g
            if a[w] == "M":
                if a[w-1] == "C":
                    g = M-C + g
                else:
                    g = M + g
        print(g)
        return g

sol = Solution()
sol.romanToInt("DCXXI")

