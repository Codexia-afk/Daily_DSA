class Solution(object):

    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        total_n = n + k - 1
        r = 2 * k

        if r > total_n:
            return 0

        # Compute C(total_n, r) % MOD directly
        num = 1
        den = 1

        for i in range(r):
            num = (num * (total_n - i)) % MOD
            den = (den * (i + 1)) % MOD

        # Fermat's Little Theorem: den^(-1) = pow(den, MOD - 2, MOD)
        return (num * pow(den, MOD - 2, MOD)) % MOD