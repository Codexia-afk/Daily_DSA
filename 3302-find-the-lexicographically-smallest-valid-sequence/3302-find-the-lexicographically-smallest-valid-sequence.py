class Solution(object):

    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)

        # last[j] stores the largest index in word1 from which word2[j:]
        # can be matched as a suffix sequence.
        last = [-1] * m
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        can_skip = True  # Tracks whether we can still make 1 character change/mismatch
        j = 0  # Index for word2

        for i in range(n):
            if j == m:
                break

            # Choice 1: Exact character match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Choice 2: Mismatch / Skip character using the allowed 1 change
            elif can_skip and (j == m - 1 or i < last[j + 1]):
                can_skip = False
                ans.append(i)
                j += 1

        return ans if j == m else []