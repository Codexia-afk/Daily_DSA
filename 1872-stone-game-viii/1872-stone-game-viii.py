class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        
        # Compute prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i - 1]
            
        # dp stores the maximum score difference achievable starting at or after index i
        # Base case: picking all stones up to index n - 1 leaves no more moves
        dp = stones[-1]
        
        # Iterate backwards from the second-to-last index down to index 1 (since x > 1)
        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)
            
        return dp