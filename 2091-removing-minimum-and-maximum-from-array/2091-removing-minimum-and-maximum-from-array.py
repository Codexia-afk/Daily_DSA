class Solution(object):

    def minimumDeletions(self, nums):
        n = len(nums)
        if n == 1:
            return 1

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)

        remove_both_front = b + 1
        remove_both_back = n - a
        remove_both_sides = (a + 1) + (n - b)

        return min(remove_both_front, remove_both_back, remove_both_sides)