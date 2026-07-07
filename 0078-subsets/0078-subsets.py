class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []

        def backtrack(index):
            if index == len(nums):
                ans.append(path[:])
                return

            # Do not take nums[index]
            backtrack(index + 1)

            # Take nums[index]
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()

        backtrack(0)
        return ans
        