class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []

        def backtrack(start):
            if len(path) == k:
                ans.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return ans
        