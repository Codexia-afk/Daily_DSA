class Solution(object):

    def maxSum(self, nums, k):
        MOD = 10**9 + 7

        # 1. Count the occurrences of set bits at each bit position (0 to 30)
        bit_counts = [0] * 31
        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b] += 1

        # 2. Greedily form k largest numbers
        ans = 0
        for _ in range(k):
            val = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    val |= 1 << b
                    bit_counts[b] -= 1
            ans = (ans + val * val) % MOD

        return ans
        