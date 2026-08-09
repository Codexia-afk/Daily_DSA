class Solution(object):

    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            
            if i >= n:
                return 0
            
            if i + 2 * m >= n:
                return suffix_sum[i]

            if (i, m) in memo:
                return memo[(i, m)]

            max_stones = 0
            
            for x in range(1, 2 * m + 1):
                
                next_score = dp(i + x, max(m, x))
                current_score = suffix_sum[i] - next_score
                max_stones = max(max_stones, current_score)

            memo[(i, m)] = max_stones
            return max_stones

        return dp(0, 1)