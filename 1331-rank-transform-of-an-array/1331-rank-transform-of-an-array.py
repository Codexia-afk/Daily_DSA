class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_unique = sorted(set(arr))

        rank = {}
        for i in range(len(sorted_unique)):
            rank[sorted_unique[i]] = i + 1

        return [rank[num] for num in arr]