class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        digit_sum = 0

        for ch in str(n):
            if ch != '0':
                digit = ord(ch) - ord('0')
                x = x * 10 + digit
                digit_sum += digit

        return x * digit_sum