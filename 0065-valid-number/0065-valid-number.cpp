class Solution {
public:
    bool isNumber(string s) {
        bool seenDigit = false;
        bool seenDot = false;
        bool seenExp = false;

        for (int i = 0; i < s.size(); i++) {
            char ch = s[i];

            if (isdigit(ch)) {
                seenDigit = true;
            }
            else if (ch == '+' || ch == '-') {
                if (i != 0 && s[i - 1] != 'e' && s[i - 1] != 'E') {
                    return false;
                }
            }
            else if (ch == '.') {
                if (seenDot || seenExp) {
                    return false;
                }
                seenDot = true;
            }
            else if (ch == 'e' || ch == 'E') {
                if (seenExp || !seenDigit) {
                    return false;
                }
                seenExp = true;
                seenDigit = false;
            }
            else {
                return false;
            }
        }

        return seenDigit;
    }
};