class Solution(object):

    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        idx = 1

        first_cp = -1
        prev_cp = -1
        min_dist = float("inf")

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (
                curr.val < prev.val and curr.val < curr.next.val
            ):
                if first_cp == -1:
                    first_cp = idx
                else:
                    min_dist = min(min_dist, idx - prev_cp)
                prev_cp = idx

            prev = curr
            curr = curr.next
            idx += 1

        if first_cp == -1 or first_cp == prev_cp:
            return [-1, -1]

        return [min_dist, prev_cp - first_cp]