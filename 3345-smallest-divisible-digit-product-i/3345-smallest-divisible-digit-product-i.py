class Solution(object):

    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """

        def get_digit_product(num):
            prod = 1
            for digit in str(num):
                prod *= int(digit)
            return prod

        curr = n
        while True:
            if get_digit_product(curr) % t == 0:
                return curr
            curr += 1