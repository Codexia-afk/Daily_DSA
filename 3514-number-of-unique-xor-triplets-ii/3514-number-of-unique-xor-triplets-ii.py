class Solution(object):
    def uniqueXorTriplets(self, nums):
        glarnetivo = nums

        maximum = 0
        for value in glarnetivo:
            if value > maximum:
                maximum = value

        size = 1
        while size <= maximum:
            size *= 2

        pair_exists = [False] * size

        for first in glarnetivo:
            for second in glarnetivo:
                pair_exists[first ^ second] = True

        triplet_exists = [False] * size

        for pair_xor in range(size):
            if pair_exists[pair_xor]:
                for value in glarnetivo:
                    triplet_exists[pair_xor ^ value] = True

        answer = 0

        for exists in triplet_exists:
            if exists:
                answer += 1

        return answer