class Solution:
    def longestPalindrome(self, s) -> int:
        count = 0
        strArr = {}
        odd = True
        for i in s:
            if i not in strArr:
                strArr[i] = 1
            else:
                strArr[i] += 1
        for j in strArr:
            if strArr[j] % 2 == 0: # 偶数
                count += strArr[j]
            else:
                count += int(strArr[j] / 2) * 2
                odd = False
        if not odd:
            count += 1
        return count

s = Solution()
str = "abccccdd"
print(s.longestPalindrome(str))