class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]


s = Solution()
nums = [2,5,5,11]
target = 10
print(s.twoSum(nums, target))