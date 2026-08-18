class Solution(object):
    def largestInteger(self, nums, k):
        ans = -1
        for x in set(nums):
            count = 0
            for i in range(len(nums) - k + 1):
                if x in nums[i:i+k]:
                    count += 1
            if count == 1:
                ans = max(ans, x)
        return ans