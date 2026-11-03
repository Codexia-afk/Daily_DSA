class Solution(object):

    def minMoves(self, nums):
        max_val = max(nums)
        return sum(max_val - x for x in nums)