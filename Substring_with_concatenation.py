from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        ans = []

        for i in range(len(s) - total_len + 1):
            seen = {}

            for j in range(word_count):
                word = s[i + j * word_len : i + (j + 1) * word_len]

                if word not in target:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > target[word]:
                    break

            else:
                ans.append(i)

        return ans
