class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        active = 0

        for ch in s:
            if ch == '1':
                active += 1

        t = '1' + s + '1'

        zero_blocks = []
        i = 0

        while i < len(t):
            if t[i] == '0':
                length = 0

                while i < len(t) and t[i] == '0':
                    length += 1
                    i += 1

                zero_blocks.append(length)
            else:
                i += 1

        maximum_gain = 0

        for i in range(len(zero_blocks) - 1):
            gain = zero_blocks[i] + zero_blocks[i + 1]

            if gain > maximum_gain:
                maximum_gain = gain

        return active + maximum_gain