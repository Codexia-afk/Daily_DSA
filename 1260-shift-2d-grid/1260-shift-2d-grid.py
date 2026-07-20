class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols

        k = k % total
        result = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                old_position = row * cols + col
                new_position = (old_position + k) % total

                new_row = new_position // cols
                new_col = new_position % cols

                result[new_row][new_col] = grid[row][col]

        return result