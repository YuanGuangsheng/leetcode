class Solution:
    def searchInsert(self, nums, target) -> int:
        last = len(nums) - 1
        for i in range(len(nums)):
            if nums[last] < target:
                return last + 1
            if nums[i] >= target:
                return i

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))