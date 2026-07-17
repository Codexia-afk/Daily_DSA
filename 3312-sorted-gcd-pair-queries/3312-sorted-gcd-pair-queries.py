class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        maximum = 0

        for num in nums:
            if num > maximum:
                maximum = num

        frequency = [0] * (maximum + 1)

        for num in nums:
            frequency[num] += 1

        exact_gcd = [0] * (maximum + 1)

        for g in range(maximum, 0, -1):
            divisible_count = 0

            multiple = g
            while multiple <= maximum:
                divisible_count += frequency[multiple]
                multiple += g

            
            pair_count = divisible_count * (divisible_count - 1) // 2

            
            multiple = g * 2
            while multiple <= maximum:
                pair_count -= exact_gcd[multiple]
                multiple += g

            exact_gcd[g] = pair_count

        
        prefix_pairs = [0] * (maximum + 1)

        for g in range(1, maximum + 1):
            prefix_pairs[g] = prefix_pairs[g - 1] + exact_gcd[g]

        answer = []

        for query in queries:
            
            left = 1
            right = maximum

            while left < right:
                middle = (left + right) // 2

                if prefix_pairs[middle] > query:
                    right = middle
                else:
                    left = middle + 1

            answer.append(left)

        return answer