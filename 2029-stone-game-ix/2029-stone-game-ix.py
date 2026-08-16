class Solution(object):

    def stoneGameIX(self, stones):
        c0 = c1 = c2 = 0
        for x in stones:
            rem = x % 3
            if rem == 0:
                c0 += 1
            elif rem == 1:
                c1 += 1
            else:
                c2 += 1

        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        else:
            return abs(c1 - c2) > 2