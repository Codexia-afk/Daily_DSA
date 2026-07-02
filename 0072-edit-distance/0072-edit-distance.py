class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        dp = [0] * (n + 1)

        for j in range(n + 1):
            dp[j] = j

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                temp = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(prev, dp[j], dp[j - 1])

                prev = temp

        return dp[n]      