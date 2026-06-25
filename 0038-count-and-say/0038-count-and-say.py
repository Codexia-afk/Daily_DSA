class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"

        for _ in range(n - 1):
            new_ans = []
            count = 1

            for i in range(1, len(ans)):
                if ans[i] == ans[i - 1]:
                    count += 1
                else:
                    new_ans.append(str(count))
                    new_ans.append(ans[i - 1])
                    count = 1

            new_ans.append(str(count))
            new_ans.append(ans[-1])

            ans = "".join(new_ans)

        return ans