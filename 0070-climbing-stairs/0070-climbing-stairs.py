class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second     