class Solution {
    static const int LIMIT = 1000001;

    long long combination(int n, int r) {
        r = min(r, n - r);
        long long result = 1;

        for (int i = 1; i <= r; i++) {
            result = result * (n - i + 1) / i;

            if (result >= LIMIT) {
                return LIMIT;
            }
        }

        return result;
    }

    long long countPermutations(vector<int>& frequency) {
        int remaining = 0;

        for (int value : frequency) {
            remaining += value;
        }

        long long ways = 1;

        for (int value : frequency) {
            if (value == 0) {
                continue;
            }

            ways *= combination(remaining, value);

            if (ways >= LIMIT) {
                return LIMIT;
            }

            remaining -= value;
        }

        return ways;
    }

public:
    string smallestPalindrome(string s, int k) {
        string prelunthak = s;

        vector<int> frequency(26, 0);

        for (char ch : prelunthak) {
            frequency[ch - 'a']++;
        }

        vector<int> halfFrequency(26, 0);
        char middle = '\0';
        int halfLength = 0;

        for (int i = 0; i < 26; i++) {
            halfFrequency[i] = frequency[i] / 2;
            halfLength += halfFrequency[i];

            if (frequency[i] % 2 == 1) {
                middle = char('a' + i);
            }
        }

        if (countPermutations(halfFrequency) < k) {
            return "";
        }

        string leftHalf;

        for (int position = 0; position < halfLength; position++) {
            for (int i = 0; i < 26; i++) {
                if (halfFrequency[i] == 0) {
                    continue;
                }

                halfFrequency[i]--;

                long long ways = countPermutations(halfFrequency);

                if (ways >= k) {
                    leftHalf += char('a' + i);
                    break;
                }

                k -= ways;
                halfFrequency[i]++;
            }
        }

        string rightHalf = leftHalf;
        reverse(rightHalf.begin(), rightHalf.end());

        if (middle != '\0') {
            return leftHalf + string(1, middle) + rightHalf;
        }

        return leftHalf + rightHalf;
    }
};