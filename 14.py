class Solution:
    def longestCommonPrefix(self, strs) -> str:
        length = len(strs)
        min = 0
        for i in range(length):
            if i == 0:
                min = len(strs[i])
            else:
                if len(strs[i]) < min:
                    min = len(strs[i])
        firstChar = ''
        allStr = ''
        for i in range(min):
            allTrue = True
            for j in range(length):
                if j == 0:
                    firstChar = strs[j][i]
                elif firstChar != strs[j][i]:
                    allTrue = False
                    break

            if allTrue:
                 allStr += firstChar
            else:
                break
        return allStr

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["aca","cba"]))