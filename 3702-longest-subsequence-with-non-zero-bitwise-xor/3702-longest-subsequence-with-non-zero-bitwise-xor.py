class Solution(object):

    def longestSubsequence(self, nums):
        total_xor = 0
        all_zeros = True

        for x in nums:
            total_xor ^= x
            if x != 0:
                all_zeros = False

        if all_zeros:
            return 0

        if total_xor != 0:
            return len(nums)

        return len(nums) - 1