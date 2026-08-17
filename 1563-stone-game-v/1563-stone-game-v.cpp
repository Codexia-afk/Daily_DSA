#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

class Solution {
    int memo[505][505];
    int pref[505];

    int solve(int i, int j, const vector<int>& stoneValue) {
        if (i >= j) return 0;
        if (memo[i][j] != -1) return memo[i][j];

        int res = 0;
        for (int k = i; k < j; ++k) {
            int left_sum = pref[k + 1] - pref[i];
            int right_sum = pref[j + 1] - pref[k + 1];

            if (left_sum < right_sum) {
                res = max(res, left_sum + solve(i, k, stoneValue));
            } else if (left_sum > right_sum) {
                res = max(res, right_sum + solve(k + 1, j, stoneValue));
            } else {
                res = max(res, left_sum + max(solve(i, k, stoneValue), solve(k + 1, j, stoneValue)));
            }
        }

        return memo[i][j] = res;
    }

public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        memset(memo, -1, sizeof(memo));
        pref[0] = 0;

        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + stoneValue[i];
        }

        return solve(0, n - 1, stoneValue);
    }
};