"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        q = deque([root])

        while q:
            size = len(q)
            prev = None

            for _ in range(size):
                node = q.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            prev.next = None

        return root