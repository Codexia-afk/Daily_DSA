class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        ans = []

        for num in range(min(nums), max(nums) + 1):
            if num not in s:
                ans.append(num)

        return ans