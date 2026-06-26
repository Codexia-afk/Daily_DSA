class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans