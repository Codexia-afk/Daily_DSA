class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int maximum = 0;

        for (int num : nums) {
            maximum = max(maximum, num);
        }

        vector<long long> frequency(maximum + 1, 0);

        for (int num : nums) {
            frequency[num]++;
        }

        // exactGcd[g] = number of pairs whose GCD is exactly g
        vector<long long> exactGcd(maximum + 1, 0);

        for (int g = maximum; g >= 1; g--) {
            long long divisibleCount = 0;

            // Count numbers divisible by g
            for (int multiple = g; multiple <= maximum; multiple += g) {
                divisibleCount += frequency[multiple];
            }

            // Number of pairs where both values are divisible by g
            long long pairCount =
                divisibleCount * (divisibleCount - 1) / 2;

            // Remove pairs whose exact GCD is a larger multiple of g
            for (int multiple = g * 2;
                 multiple <= maximum;
                 multiple += g) {
                pairCount -= exactGcd[multiple];
            }

            exactGcd[g] = pairCount;
        }

        // prefixPairs[g] = number of pair GCD values <= g
        vector<long long> prefixPairs(maximum + 1, 0);

        for (int g = 1; g <= maximum; g++) {
            prefixPairs[g] =
                prefixPairs[g - 1] + exactGcd[g];
        }

        vector<int> answer;

        for (long long query : queries) {
            int left = 1;
            int right = maximum;

            while (left < right) {
                int middle = left + (right - left) / 2;

                if (prefixPairs[middle] > query) {
                    right = middle;
                } else {
                    left = middle + 1;
                }
            }

            answer.push_back(left);
        }

        return answer;
    }
};