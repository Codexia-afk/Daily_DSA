from collections import deque


class Solution(object):

    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0
        litter_map = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start_r, start_c = r, c
                elif classroom[r][c] == "L":
                    litter_map[(r, c)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        target_mask = (1 << litter_count) - 1

        # max_energy[r][c][mask] records the maximum remaining energy seen
        max_energy = [
            [[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)
        ]

        q = deque([(start_r, start_c, 0, energy, 0)])
        max_energy[start_r][start_c][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, mask, cur_energy, moves = q.popleft()

            if mask == target_mask:
                return moves

            if cur_energy <= 0 and classroom[r][c] != "R":
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                    next_energy = cur_energy - 1

                    if next_energy < 0:
                        continue

                    cell = classroom[nr][nc]
                    next_mask = mask

                    if cell == "L" and (nr, nc) in litter_map:
                        next_mask |= 1 << litter_map[(nr, nc)]

                    if cell == "R":
                        next_energy = energy

                    if next_energy > max_energy[nr][nc][next_mask]:
                        max_energy[nr][nc][next_mask] = next_energy
                        q.append((nr, nc, next_mask, next_energy, moves + 1))

        return -1