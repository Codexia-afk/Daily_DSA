class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        required = len(t)
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in need:
                if need[ch] > 0:
                    required -= 1
                need[ch] -= 1
            else:
                need[ch] = -1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                need[left_char] += 1

                if need[left_char] > 0:
                    required += 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
        