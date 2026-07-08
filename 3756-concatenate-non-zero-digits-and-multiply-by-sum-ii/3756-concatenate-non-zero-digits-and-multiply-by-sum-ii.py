class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10 ** 9 + 7
        n = len(s)

        prefCnt = [0] * (n + 1)
        prefSum = [0] * (n + 1)
        prefVal = [0] * (n + 1)
        pow10 = [1] * (n + 1)

        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        for i, ch in enumerate(s):
            digit = ord(ch) - ord('0')

            prefCnt[i + 1] = prefCnt[i]
            prefSum[i + 1] = prefSum[i] + digit
            prefVal[i + 1] = prefVal[i]

            if digit != 0:
                prefCnt[i + 1] += 1
                prefVal[i + 1] = (prefVal[i] * 10 + digit) % MOD

        ans = []

        for l, r in queries:
            nonzero_len = prefCnt[r + 1] - prefCnt[l]

            x = (prefVal[r + 1] - prefVal[l] * pow10[nonzero_len]) % MOD
            digit_sum = prefSum[r + 1] - prefSum[l]

            ans.append((x * digit_sum) % MOD)

        return ans