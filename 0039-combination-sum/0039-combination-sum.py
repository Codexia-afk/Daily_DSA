class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []

        def backtrack(start, total, path):
            if total == target:
                ans.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])

                # i, not i + 1, because same number can be reused
                backtrack(i, total + candidates[i], path)

                path.pop()

        backtrack(0, 0, [])
        return ans
        