class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = mul + res[i + j + 1]

                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        ans = []
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        while i < len(res):
            ans.append(str(res[i]))
            i += 1

        return "".join(ans)