class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        max_value = max(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
        dp[0][0] = 1

        for value in nums:
            new_dp = [row[:] for row in dp]

            for g1 in range(max_value + 1):
                for g2 in range(max_value + 1):
                    count = dp[g1][g2]

                    if count == 0:
                        continue

                    new_g1 = value if g1 == 0 else gcd(g1, value)
                    new_dp[new_g1][g2] = (
                        new_dp[new_g1][g2] + count
                    ) % MOD

                    new_g2 = value if g2 == 0 else gcd(g2, value)
                    new_dp[g1][new_g2] = (
                        new_dp[g1][new_g2] + count
                    ) % MOD

            dp = new_dp

        answer = 0
        for g in range(1, max_value + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer