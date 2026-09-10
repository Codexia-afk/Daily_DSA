class Solution(object):

    def averageOfSubtree(self, root):
        self.count = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_nodes = 1 + left_nodes + right_nodes

            if total_sum // total_nodes == node.val:
                self.count += 1

            return total_sum, total_nodes

        dfs(root)
        return self.count