class Solution(object):
    def maxTotalValue(self, nums, k):
        return (max(nums) - min(nums)) * k
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
