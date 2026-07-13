class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        nums = "123456789"
        ans = []

        for length in range(2, 10):
            for start in range(10 - length):
                num = int(nums[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans