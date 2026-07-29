class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        limit = 1000001
        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch) - ord('a')] += 1

        half_frequency = [0] * 26
        half_length = 0
        middle = ""

        for i in range(26):
            half_frequency[i] = frequency[i] // 2
            half_length += half_frequency[i]

            if frequency[i] % 2 == 1:
                middle = chr(ord('a') + i)

        def combination(n, r):
            r = min(r, n - r)
            result = 1

            for i in range(1, r + 1):
                result = result * (n - i + 1) // i

                if result >= limit:
                    return limit

            return result

        def count_permutations(counts):
            remaining = sum(counts)
            ways = 1

            for count in counts:
                if count == 0:
                    continue

                ways *= combination(remaining, count)

                if ways >= limit:
                    return limit

                remaining -= count

            return ways

        if count_permutations(half_frequency) < k:
            return ""

        left_half = []

        for _ in range(half_length):
            for i in range(26):
                if half_frequency[i] == 0:
                    continue

                half_frequency[i] -= 1
                ways = count_permutations(half_frequency)

                if ways >= k:
                    left_half.append(chr(ord('a') + i))
                    break

                k -= ways
                half_frequency[i] += 1

        left_half = "".join(left_half)
        return left_half + middle + left_half[::-1]
        