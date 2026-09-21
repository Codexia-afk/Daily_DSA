class Solution(object):

    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for x in nums:
            v = x % k
            new_dp = [0] * k
            # Single-element subarray [x]
            new_dp[v] = (new_dp[v] + 1)

            # Extend previous subarrays ending at index - 1
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * v) % k] += dp[r]

            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result