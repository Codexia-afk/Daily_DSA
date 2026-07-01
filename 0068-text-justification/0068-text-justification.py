class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        i = 0

        while i < len(words):
            line_len = len(words[i])
            j = i + 1

            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            word_count = j - i

            # Last line or only one word
            if j == len(words) or word_count == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_word_len = sum(len(word) for word in words[i:j])
                total_spaces = maxWidth - total_word_len
                gaps = word_count - 1

                space_each = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""
                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        spaces = space_each + (1 if extra > 0 else 0)
                        line += " " * spaces
                        if extra > 0:
                            extra -= 1

            ans.append(line)
            i = j

        return ans