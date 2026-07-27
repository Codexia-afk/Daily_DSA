# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True

        while queue:
            size = len(queue)
            level = [0] * size

            for i in range(size):
                node = queue.pop(0)

                if left_to_right:
                    index = i
                else:
                    index = size - 1 - i

                level[index] = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right

        return result
        