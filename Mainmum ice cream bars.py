class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_cost = max(costs)
        count = [0] * (max_cost + 1)

        for cost in costs:
            count[cost] += 1

        ans = 0

        for cost in range(1, max_cost + 1):
            while count[cost] > 0 and coins >= cost:
                coins -= cost
                ans += 1
                count[cost] -= 1

        return ans
