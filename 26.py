class Solution:
    def removeDuplicates(self, nums) -> int:
        before = None
        j = 0
        for i in range(len(nums)):
            n = nums[j]
            if i == 0:
                before = n
                j += 1
            else:
                if before == n:
                    del nums[j]
                else:
                    before = n
                    j += 1

        return len(nums)

s = Solution()
nums = [1,1,2]
print(s.removeDuplicates(nums))
print(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)