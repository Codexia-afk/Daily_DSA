class Solution(object):
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    bit = 1 << int(board[r][c])
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def dfs(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            b = (r // 3) * 3 + c // 3

            for d in range(1, 10):
                bit = 1 << d
                if rows[r] & bit or cols[c] & bit or boxes[b] & bit:
                    continue

                board[r][c] = str(d)
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if dfs(idx + 1):
                    return True

                board[r][c] = '.'
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            return False

        dfs(0)