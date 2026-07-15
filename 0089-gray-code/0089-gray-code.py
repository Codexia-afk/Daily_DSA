class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        for i in range(1 << n):
            result.append(i ^ (i >> 1))

        return result