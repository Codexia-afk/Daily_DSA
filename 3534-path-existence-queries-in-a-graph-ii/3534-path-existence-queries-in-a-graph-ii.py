class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        order = sorted(range(n), key=lambda i: nums[i])

        sorted_values = [nums[i] for i in order]

        position = [0] * n
        for i in range(n):
            position[order[i]] = i

        farthest = [0] * n
        right = 0

        for left in range(n):
            if right < left:
                right = left

            while (right + 1 < n and
                   sorted_values[right + 1] - sorted_values[left] <= maxDiff):
                right += 1

            farthest[left] = right

        log = 1
        while (1 << log) <= n:
            log += 1

        jump = [[0] * n for _ in range(log)]
        jump[0] = farthest[:]

        for level in range(1, log):
            for i in range(n):
                jump[level][i] = jump[level - 1][jump[level - 1][i]]

        answer = []

        for u, v in queries:
            start = position[u]
            target = position[v]

            if start > target:
                start, target = target, start

            if start == target:
                answer.append(0)
                continue

            current = start
            steps = 0

            for level in range(log - 1, -1, -1):
                next_position = jump[level][current]

                if next_position < target and next_position > current:
                    current = next_position
                    steps += 1 << level

            if farthest[current] >= target:
                answer.append(steps + 1)
            else:
                answer.append(-1)

        return answer
       

            
            