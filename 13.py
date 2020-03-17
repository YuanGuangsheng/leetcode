class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        doubles = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        total = 0
        skip = False
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if i < len(s) - 1 and (s[i]+s[i+1] in doubles):
                total += doubles[s[i]+s[i+1]]
                skip = True
            else:
                total += vals[s[i]]

        return total

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("IX"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))