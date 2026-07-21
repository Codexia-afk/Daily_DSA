class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        parts = []

        def backtrack(index):
        
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

           
            remaining_digits = len(s) - index
            remaining_parts = 4 - len(parts)

            if remaining_digits < remaining_parts:
                return

            if remaining_digits > remaining_parts * 3:
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]


                if len(part) > 1 and part[0] == '0':
                    break

                value = int(part)

                if value > 255:
                    break

                parts.append(part)
                backtrack(index + length)
                parts.pop()

        backtrack(0)
        return result