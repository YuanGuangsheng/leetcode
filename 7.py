class Solution:
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x // 10

        value = 0
        for i in range(len(nums)):
            value += nums[i] * (10 ** (len(nums) - i - 1))

        if value > (2 ** 31) - 1:
            return 0

        return value * sign

s = Solution()
print(s.reverse(123))
# print(s.reverse(-123))
# print(s.reverse(120))
# print(s.reverse(1534236469))