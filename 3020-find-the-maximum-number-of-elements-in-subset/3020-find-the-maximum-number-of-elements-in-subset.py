from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in count:
            if count[1] % 2 == 1:
                ans = max(ans, count[1])
            else:
                ans = max(ans, count[1] - 1)

        for x in count:
            if x == 1:
                continue

            length = 0
            cur = x

            while cur in count:
                if count[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    break

                if cur > 10 ** 9:
                    break

            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans 