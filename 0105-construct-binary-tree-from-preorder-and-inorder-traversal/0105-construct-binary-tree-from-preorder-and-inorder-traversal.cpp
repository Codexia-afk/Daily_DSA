/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    unordered_map<int, int> inorderIndex;
    int preorderIndex = 0;

    TreeNode* build(vector<int>& preorder, int left, int right) {
        if (left > right) {
            return nullptr;
        }

        int rootValue = preorder[preorderIndex];
        preorderIndex++;

        TreeNode* root = new TreeNode(rootValue);
        int middle = inorderIndex[rootValue];

        root->left = build(preorder, left, middle - 1);
        root->right = build(preorder, middle + 1, right);

        return root;
    }

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inorderIndex[inorder[i]] = i;
        }

        return build(preorder, 0, inorder.size() - 1);
    }
};