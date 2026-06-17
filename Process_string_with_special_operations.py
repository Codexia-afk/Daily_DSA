class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)

        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass

        if k >= length:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == length - 1:
                    return ch
                length -= 1

            elif ch == '*':
                length += 1

            elif ch == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half

            elif ch == '%':
                k = length - 1 - k

        return '.'
        
