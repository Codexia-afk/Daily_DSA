class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        # Left to right pass
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0]
            )

        # Right to left pass
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0]
            )

        ans = 0

        # Find maximum possible peak between consecutive restrictions
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            dist = x2 - x1
            ans = max(ans, (h1 + h2 + dist) // 2)

        return ans
