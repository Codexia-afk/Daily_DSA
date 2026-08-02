# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                if remaining == node.val:
                    result.append(path[:])      
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)

            path.pop()     

        dfs(root, targetSum, [])

        return result
        