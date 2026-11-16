class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            nxt = []
            for i in range(0, len(s), k):
                group_sum = 0
                for j in range(i, min(i + k, len(s))):
                    group_sum += ord(s[j]) - 48
                nxt.append(str(group_sum))
            s = "".join(nxt)
        return s  