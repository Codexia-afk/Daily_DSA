class Solution {
public:
    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        int n = online.size();

        vector<vector<pair<int,int>>> graph(n);
        vector<int> indegree(n, 0);

        int mxCost = 0;

        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].push_back({v, w});
            indegree[v]++;
            mxCost = max(mxCost, w);
        }

        // Topological Order
        vector<int> topo;
        queue<int> q;
        vector<int> deg = indegree;

        for (int i = 0; i < n; i++)
            if (deg[i] == 0) q.push(i);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            topo.push_back(u);
            for (auto &p : graph[u]) {
                if (--deg[p.first] == 0)
                    q.push(p.first);
            }
        }

        auto check = [&](int limit) {
            const long long INF = (1LL << 60);
            vector<long long> dist(n, INF);
            dist[0] = 0;

            for (int u : topo) {
                if (dist[u] == INF) continue;

                if (u != 0 && u != n - 1 && !online[u]) continue;

                for (auto &[v, w] : graph[u]) {
                    if (w < limit) continue;
                    if (v != 0 && v != n - 1 && !online[v]) continue;

                    dist[v] = min(dist[v], dist[u] + (long long)w);
                }
            }

            return dist[n - 1] <= k;
        };

        int lo = 0, hi = mxCost, ans = -1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (check(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return ans;
    }
};