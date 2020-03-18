class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = {
            "(" : [],
            "[" : [],
            "{" : [],
        }

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack[s[i]].append(i)
            else:
                find = "("
                if s[i] == "]":
                    find = "["
                if s[i] == "}":
                    find = "{"

                if len(stack[find]) == 0:
                    return False

                j = stack[find].pop()
                if (i - j) % 2 == 0:
                    return False

        if len(stack["("]) > 0 or len(stack["["]) > 0 or len(stack["{"]) > 0:
            return False

        return True

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("(("))