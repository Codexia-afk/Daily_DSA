class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        total = 0

        for i in range(n):
            total += (i // 8) + 1

        return total
        