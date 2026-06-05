class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

         
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) +
                            min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1
        
