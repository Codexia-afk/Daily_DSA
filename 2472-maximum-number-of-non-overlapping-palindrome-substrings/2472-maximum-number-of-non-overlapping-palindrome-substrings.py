class Solution(object):

    def maxPalindromes(self, s, k):
        n = len(s)
        ans = 0
        last_end = -1

        # Check all possible palindrome centers:
        # 2*n - 1 centers (single characters or pairs of adjacent characters)
        for center in range(2 * n - 1):
            l = center // 2
            r = l + (center % 2)

            while l >= 0 and r < n and s[l] == s[r]:
                # If we formed a palindrome of length >= k
                if r - l + 1 >= k:
                    # Check if it doesn't overlap with our previously picked palindrome
                    if l > last_end:
                        ans += 1
                        last_end = r
                    # Crucial greedy observation:
                    # Once a valid palindrome is found for this center, expanding it further
                    # only consumes more characters on the right without adding to our count.
                    break
                l -= 1
                r += 1

        return ans