class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0

        for ch in reversed(s):
            curr = roman[ch]

            if curr < prev:
                total -= curr
            else:
                total += curr

            prev = curr

        return total
        
        """
        :type s: str
        :rtype: int
        """
        
