class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10 ** 9 + 7

        m = r - l + 1

        if n == 1:
            return m

        dp_up = [0] * m
        dp_down = [0] * m

        for i in range(m):
            dp_up[i] = i
            dp_down[i] = m - 1 - i

        if n == 2:
            return (m * (m - 1)) % MOD

        for _ in range(3, n + 1):

            prefix_up = [0] * (m + 1)
            prefix_down = [0] * (m + 1)

            for i in range(m):
                prefix_up[i + 1] = (prefix_up[i] + dp_up[i]) % MOD
                prefix_down[i + 1] = (prefix_down[i] + dp_down[i]) % MOD

            total_up = prefix_up[m]
            total_down = prefix_down[m]

            new_up = [0] * m
            new_down = [0] * m

            for i in range(m):
                new_up[i] = prefix_down[i]
                new_down[i] = (total_up - prefix_up[i + 1]) % MOD

            dp_up = new_up
            dp_down = new_down

        return (sum(dp_up) + sum(dp_down)) % MOD
