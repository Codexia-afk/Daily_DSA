class Solution(object):
    def pivotArray(self, nums, pivot):
        smaller = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        return smaller + equal + greater
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
