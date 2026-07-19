class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_position = {}

        for i in range(len(s)):
            last_position[s[i]] = i

        stack = []
        used = set()

        for i in range(len(s)):
            ch = s[i]

            
            if ch in used:
                continue

            while (
                stack
                and stack[-1] > ch
                and last_position[stack[-1]] > i
            ):
                removed = stack.pop()
                used.remove(removed)

            stack.append(ch)
            used.add(ch)

        return "".join(stack)   