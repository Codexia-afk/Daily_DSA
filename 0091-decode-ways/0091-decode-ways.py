class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            current = 0

            if s[i] != "0":
                current += prev1

            two_digit = int(s[i - 1:i + 1])

            if 10 <= two_digit <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1