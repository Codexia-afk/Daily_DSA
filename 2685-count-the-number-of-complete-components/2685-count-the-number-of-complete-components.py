class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True

            node_count = 0
            degree_sum = 0

            while stack:
                node = stack.pop()
                node_count += 1
                degree_sum += len(graph[node])

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            edge_count = degree_sum // 2
            required_edges = node_count * (node_count - 1) // 2

            if edge_count == required_edges:
                answer += 1

        return answer