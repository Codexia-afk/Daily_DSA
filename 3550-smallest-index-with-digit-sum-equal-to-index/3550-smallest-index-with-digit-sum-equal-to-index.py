class Solution(object):

    def smallestIndex(self, nums):
        for i, val in enumerate(nums):
            # Sum the digits of val
            s = 0
            n = val
            while n > 0:
                s += n % 10
                n //= 10

            if s == i:
                return i

        return -1