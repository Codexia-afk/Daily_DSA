import java.util.*;

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";

        int[] need = new int[128];

        for (char ch : t.toCharArray()) {
            need[ch]++;
        }

        int left = 0;
        int required = t.length();

        int minLen = Integer.MAX_VALUE;
        int start = 0;

        for (int right = 0; right < s.length(); right++) {
            char rch = s.charAt(right);

            if (need[rch] > 0) {
                required--;
            }

            need[rch]--;

            while (required == 0) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    start = left;
                }

                char lch = s.charAt(left);
                need[lch]++;

                if (need[lch] > 0) {
                    required++;
                }

                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}