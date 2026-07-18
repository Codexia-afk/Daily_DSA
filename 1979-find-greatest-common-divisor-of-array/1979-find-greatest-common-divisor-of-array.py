class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0]
        largest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num

            if num > largest:
                largest = num

        # Euclidean algorithm
        while largest != 0:
            smallest, largest = largest, smallest % largest

        return smallest