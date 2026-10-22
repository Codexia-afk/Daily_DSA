class Solution(object):

    def minOperations(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        idx_0 = nums.index(0)

        is_increasing = all(nums[(idx_0 + i) % n] == i for i in range(n))
        is_decreasing = all(nums[(idx_0 - i) % n] == i for i in range(n))

        if not is_increasing and not is_decreasing:
            return -1

        candidates = []

        if is_increasing:
            candidates.append(idx_0)
            candidates.append((n - idx_0) % n + 2)

        if is_decreasing:
            candidates.append(1 + (n - 1 - idx_0))
            candidates.append(((idx_0 + 1) % n) + 1)

        return min(candidates)