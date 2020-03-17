class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i,j]


s = Solution()
result = s.twoSum([2,5,5,11], 10)
print(result)