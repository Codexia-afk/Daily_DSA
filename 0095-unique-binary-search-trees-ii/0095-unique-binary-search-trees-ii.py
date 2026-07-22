# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """

        def build(start, end):
            
            if start > end:
                return [None]

            all_trees = []

            for root_value in range(start, end + 1):

                left_trees = build(start, root_value - 1)
                right_trees = build(root_value + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_value)
                        root.left = left_tree
                        root.right = right_tree
                        all_trees.append(root)

            return all_trees

        return build(1, n)