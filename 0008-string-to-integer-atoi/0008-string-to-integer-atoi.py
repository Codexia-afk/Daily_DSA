class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        result = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1
            
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result