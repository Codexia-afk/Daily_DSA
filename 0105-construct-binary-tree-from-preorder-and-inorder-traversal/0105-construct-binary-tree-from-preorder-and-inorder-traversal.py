# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_index = {}

        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        preorder_index = [0]

        def build(left, right):
            if left > right:
                return None

            root_value = preorder[preorder_index[0]]
            preorder_index[0] += 1

            root = TreeNode(root_value)
            middle = inorder_index[root_value]

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(inorder) -1)
        