class Solution(object):

    def minMoves(self, nums):
        min_val = min(nums)
        return sum(x - min_val for x in nums)