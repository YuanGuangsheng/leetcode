class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1

        index = -1
        j = 0
        i = 0
        while j < len(needle) and i < len(haystack):
            c = haystack[i]
            if c == needle[j]:
                if index == -1:
                    index = i
                j += 1
                i += 1
            else:
                if index != -1:
                    i = index+1
                else:
                    i += 1
                index = -1
                j = 0

        if j != len(needle):
            return -1

        return index

s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("", ""))
print(s.strStr("a", ""))
print(s.strStr("mississippi", "issip"))
print(s.strStr("mississippi", "issipi"))
