from collections import defaultdict


class Solution(object):

    def maxSubarrayLength(self, nums, k):
        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len