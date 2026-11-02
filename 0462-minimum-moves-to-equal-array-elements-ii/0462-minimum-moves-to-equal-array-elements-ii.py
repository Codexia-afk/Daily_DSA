class Solution(object):

    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)