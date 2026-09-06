class Solution(object):

    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]