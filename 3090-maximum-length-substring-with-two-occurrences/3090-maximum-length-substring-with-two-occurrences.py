from collections import defaultdict


class Solution(object):

    def maximumLengthSubstring(self, s):
        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len