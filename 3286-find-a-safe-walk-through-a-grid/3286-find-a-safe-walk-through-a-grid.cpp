class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        deque<pair<int, int>> dq;

        dist[0][0] = grid[0][0];
        dq.push_front({0, 0});

        vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!dq.empty()) {
            auto [r, c] = dq.front();
            dq.pop_front();

            for (auto [dr, dc] : dirs) {
                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int newCost = dist[r][c] + grid[nr][nc];

                    if (newCost < dist[nr][nc]) {
                        dist[nr][nc] = newCost;

                        if (grid[nr][nc] == 0)
                            dq.push_front({nr, nc});
                        else
                            dq.push_back({nr, nc});
                    }
                }
            }
        }

        return dist[m - 1][n - 1] < health;
    }
};