class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        visited = [False] * (n + 1)
        ans = float("inf")

        def dfs(node):
            nonlocal ans
            visited[node] = True

            for nei, dist in graph[node]:
                ans = min(ans, dist)
                if not visited[nei]:
                    dfs(nei)

        dfs(1)
        return ans