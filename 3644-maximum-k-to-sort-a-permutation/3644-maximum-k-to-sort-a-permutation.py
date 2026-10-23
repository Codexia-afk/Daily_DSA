class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = None

        for i, x in enumerate(nums):
            if x != i:
                ans = x if ans is None else (ans & x)

        return 0 if ans is None else ans
        