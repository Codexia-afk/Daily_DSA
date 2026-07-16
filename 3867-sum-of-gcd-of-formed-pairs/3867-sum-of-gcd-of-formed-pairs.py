class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        prefix_gcd = []
        current_max = nums[0]

        for num in nums:
            if num > current_max:
                current_max = num

            prefix_gcd.append(gcd(num, current_max))

        prefix_gcd.sort()

        left = 0
        right = len(prefix_gcd) - 1
        answer = 0

        while left < right:
            answer += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return answer