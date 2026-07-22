# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def validate(node, minimum, maximum):
            if node is None:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            left_valid = validate(node.left, minimum, node.val)

            right_valid = validate(node.right, node.val, maximum)

            return left_valid and right_valid

        return validate(root, float("-inf"), float("inf"))