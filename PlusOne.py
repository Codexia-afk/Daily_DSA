class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits = [1] + digits
        return digits
