class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 
        }
        res = 0

        for i in range(len(s)):
            # i+1 < len(s): This checks that we are not at the last character (to avoid an "index out of range" error when checking s[i+1]).
            # roman[s[i]] < roman[s[i+1]]: This checks if the current numeral is smaller than the next numeral.
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]             # subtract the value of the current numeral from the result.
            else:
                res += roman[s[i]]
        return res
sol = Solution()
sol.romanToInt("MCMXCIV")

