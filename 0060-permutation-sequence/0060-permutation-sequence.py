class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        k -= 1
        ans = []

        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            ans.append(nums.pop(idx))
            k %= fact[i - 1]

        return "".join(ans)
        