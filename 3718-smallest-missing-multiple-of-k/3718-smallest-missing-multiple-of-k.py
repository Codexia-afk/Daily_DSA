class Solution(object):

    def missingMultiple(self, nums, k):
        num_set = set(nums)
        mult = k

        while mult in num_set:
            mult += k

        return mult