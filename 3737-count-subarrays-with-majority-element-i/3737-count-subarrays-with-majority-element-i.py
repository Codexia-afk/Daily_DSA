class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        offset = n + 2
        size = 2 * n + 5

        bit = [0] * size

        def update(i, delta):
            while i < size:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        prefix = 0
        ans = 0

        update(offset, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset

            ans += query(idx - 1)

            update(idx, 1)

        return ans