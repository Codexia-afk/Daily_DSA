class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}

        def solve(a, b):
            key = (a, b)

            if key in memo:
                return memo[key]

            if a == b:
                memo[key] = True
                return True

            if len(a) != len(b):
                memo[key] = False
                return False

            
            count = [0] * 26

            for i in range(len(a)):
                count[ord(a[i]) - ord('a')] += 1
                count[ord(b[i]) - ord('a')] -= 1

            for value in count:
                if value != 0:
                    memo[key] = False
                    return False

            n = len(a)

            for split in range(1, n):
                
                no_swap = (
                    solve(a[:split], b[:split]) and
                    solve(a[split:], b[split:])
                )

                if no_swap:
                    memo[key] = True
                    return True

                
                swap = (
                    solve(a[:split], b[n - split:]) and
                    solve(a[split:], b[:n - split])
                )

                if swap:
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return solve(s1, s2)  