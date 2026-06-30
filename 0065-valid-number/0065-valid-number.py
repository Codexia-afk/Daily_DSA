class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch == '+' or ch == '-':
                if i != 0 and s[i - 1] not in "eE":
                    return False

            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch == 'e' or ch == 'E':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False

            else:
                return False

        return seen_digit