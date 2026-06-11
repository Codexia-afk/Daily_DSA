class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7

        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_depth = [0]

        def dfs(node, parent, depth):
            max_depth[0] = max(max_depth[0], depth)

            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node, depth + 1)

        dfs(1, 0, 0)

        return pow(2, max_depth[0] - 1, MOD)
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
