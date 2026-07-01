from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while max_heap:
            safe, r, c = heapq.heappop(max_heap)
            safe = -safe

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_safe = min(safe, dist[nr][nc])
                    heapq.heappush(max_heap, (-new_safe, nr, nc))

        return 0