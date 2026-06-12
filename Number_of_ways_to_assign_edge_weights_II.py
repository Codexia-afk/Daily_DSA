class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = 17
        while (1 << LOG) <= n:
            LOG += 1

        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [(1, -1)]
        while stack:
            node, par = stack.pop()
            parent[0][node] = par

            for nei in graph[node]:
                if nei == par:
                    continue
                depth[nei] = depth[node] + 1
                stack.append((nei, node))

        for k in range(1, LOG):
            for v in range(1, n + 1):
                p = parent[k - 1][v]
                if p != -1:
                    parent[k][v] = parent[k - 1][p]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for k in range(LOG):
                if diff & (1 << k):
                    a = parent[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if parent[k][a] != parent[k][b]:
                    a = parent[k][a]
                    b = parent[k][b]

            return parent[0][a]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            p = lca(u, v)

            d = depth[u] + depth[v] - 2 * depth[p]

            ans.append(pow(2, d - 1, MOD))

        return ans
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
