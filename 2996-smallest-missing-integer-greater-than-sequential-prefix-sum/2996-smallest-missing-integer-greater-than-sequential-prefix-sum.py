class Solution(object):

    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total_sum += nums[i]
            else:
                break

        num_set = set(nums)
        ans = total_sum
        while ans in num_set:
            ans += 1

        return ans