class Solution(object):

    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))

        ans = [0] * n
        i = 0

        while i < n:
            j = i
            while (
                j + 1 < n and sorted_pairs[j + 1][0] - sorted_pairs[j][0] <= limit
            ):
                j += 1

            vals = [sorted_pairs[k][0] for k in range(i, j + 1)]
            indices = sorted(sorted_pairs[k][1] for k in range(i, j + 1))

            for idx, val in zip(indices, vals):
                ans[idx] = val

            i = j + 1

        return ans