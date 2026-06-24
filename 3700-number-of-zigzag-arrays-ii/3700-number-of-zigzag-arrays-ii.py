class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        if k <= 1:
            return 0
            
        M = 2 * k
        
        def multiply(A, B):
            B_T = list(zip(*B))  
            return [[sum(a * b for a, b in zip(row_A, col_B)) % MOD for col_B in B_T] for row_A in A]

        def power(A, p):
            res = [[0] * M for _ in range(M)]
            for i in range(M):
                res[i][i] = 1
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        
        T = [[0] * M for _ in range(M)]
        for u in range(k):
            
            for v in range(u + 1, k):
                T[2 * v + 1][2 * u] = 1
                
            
            for v in range(u):
                T[2 * v][2 * u + 1] = 1

        base_dp = [0] * M
        for v in range(k):
            base_dp[2 * v] = k - 1 - v      
            base_dp[2 * v + 1] = v          

        if n == 2:
            return sum(base_dp) % MOD

        T_pow = power(T, n - 2)
        ans = 0
        for i in range(M):
            row_sum = sum(T_pow[i][j] * base_dp[j] for j in range(M)) % MOD
            ans = (ans + row_sum) % MOD

        return ans