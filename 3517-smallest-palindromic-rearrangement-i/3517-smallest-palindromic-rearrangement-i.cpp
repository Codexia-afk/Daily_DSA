class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> frequency(26, 0);

        for (char ch : s) {
            frequency[ch - 'a']++;
        }

        string leftHalf = "";
        char middle = '\0';

        for (int i = 0; i < 26; i++) {
            int pairs = frequency[i] / 2;

            while (pairs > 0) {
                leftHalf += char('a' + i);
                pairs--;
            }

            if (frequency[i] % 2 == 1) {
                middle = char('a' + i);
            }
        }

        string rightHalf = leftHalf;
        reverse(rightHalf.begin(), rightHalf.end());

        if (middle != '\0') {
            return leftHalf + middle + rightHalf;
        }

        return leftHalf + rightHalf;
    }
};