class Solution:
    def removeElement(self, nums, val) -> int:
        j = 0
        for i in range(len(nums)):
            n = nums[j]
            if val == n:
                del nums[j]
            else:
                j += 1
        return len(nums)

s = Solution()
nums = [3, 2, 2, 3]
val = 3
print(s.removeElement(nums, val))
print(nums)
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(s.removeElement(nums, val))
print(nums)