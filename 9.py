class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        strX = str(x)
        length = len(strX) // 2
        for i in range(length):
            if strX[i] != strX[(len(strX) - i - 1)]:
                return False
        return True

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(0))