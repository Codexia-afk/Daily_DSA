class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        left = []
        middle = ''

        for i in range(26):
            left.append(chr(i + ord('a')) * (count[i] // 2))

            if count[i] % 2 == 1:
                middle = chr(i + ord('a'))

        left_half = ''.join(left)

        return left_half + middle + left_half[::-1]
        