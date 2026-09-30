class Solution(object):

    def maxDepthAfterSplit(self, seq):
        res = []
        depth = 0

        for ch in seq:
            if ch == "(":
                depth += 1
                res.append(depth % 2)
            else:
                res.append(depth % 2)
                depth -= 1

        return res