class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Convert the current row into histogram heights
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Find the largest rectangle in this histogram
            stack = []

            for i in range(cols + 1):
                current_height = 0 if i == cols else heights[i]

                while stack and heights[stack[-1]] > current_height:
                    height = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    max_area = max(max_area, height * width)

                stack.append(i)

        return max_area