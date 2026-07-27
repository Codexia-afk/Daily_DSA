# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        index_map = {}

        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        post_index = [len(postorder) - 1]

        def build(left, right):
            if left > right:
                return None

            root_value = postorder[post_index[0]]
            post_index[0] -= 1

            root = TreeNode(root_value)
            middle = index_map[root_value]

            root.right = build(middle + 1, right)
            root.left = build(left, middle - 1)

            return root

        return build(0, len(inorder) - 1)
        