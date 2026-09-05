class Solution(object):

    def firstStableIndex(self, nums, k):
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = (
                nums[i] if nums[i] < suffix_min[i + 1] else suffix_min[i + 1]
            )

        prefix_max = nums[0]
        for i in range(n):
            if nums[i] > prefix_max:
                prefix_max = nums[i]
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1