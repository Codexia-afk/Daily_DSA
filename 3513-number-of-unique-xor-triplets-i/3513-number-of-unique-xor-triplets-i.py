class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n <= 2:
            return n

        power = 1

        while power <= n:
            power *= 2

        return power