class Solution(object):

    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(coins)

        def count_multiples(m):
            cnt = 0
            for mask in range(1, 1 << n):
                bits = 0
                cur_lcm = 1
                for i in range(n):
                    if (mask >> i) & 1:
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])
                        if cur_lcm > m:
                            break
                if cur_lcm <= m:
                    if bits % 2 == 1:
                        cnt += m // cur_lcm
                    else:
                        cnt -= m // cur_lcm
            return cnt

        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans