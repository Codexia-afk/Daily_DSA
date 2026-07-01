import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> ans = new ArrayList<>();
        int i = 0;

        while (i < words.length) {
            int lineLen = words[i].length();
            int j = i + 1;

            while (j < words.length && lineLen + 1 + words[j].length() <= maxWidth) {
                lineLen += 1 + words[j].length();
                j++;
            }

            int wordCount = j - i;
            StringBuilder line = new StringBuilder();

            // Last line or only one word => left justify
            if (j == words.length || wordCount == 1) {
                for (int k = i; k < j; k++) {
                    line.append(words[k]);
                    if (k < j - 1) line.append(" ");
                }

                while (line.length() < maxWidth) {
                    line.append(" ");
                }
            } else {
                int totalWordLen = 0;
                for (int k = i; k < j; k++) {
                    totalWordLen += words[k].length();
                }

                int totalSpaces = maxWidth - totalWordLen;
                int gaps = wordCount - 1;

                int spaceEach = totalSpaces / gaps;
                int extra = totalSpaces % gaps;

                for (int k = i; k < j; k++) {
                    line.append(words[k]);

                    if (k < j - 1) {
                        int spaces = spaceEach + (extra > 0 ? 1 : 0);
                        for (int s = 0; s < spaces; s++) {
                            line.append(" ");
                        }
                        extra--;
                    }
                }
            }

            ans.add(line.toString());
            i = j;
        }

        return ans;
    }
}