class Solution(object):

    def checkDivisibility(self, n):
        digit_sum = 0
        digit_prod = 1

        for ch in str(n):
            d = int(ch)
            digit_sum += d
            digit_prod *= d

        total = digit_sum + digit_prod
        return n % total == 0