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
    int postorderIndex;

    TreeNode* build(vector<int>& postorder, int left, int right) {
        if (left > right) {
            return nullptr;
        }

        int rootValue = postorder[postorderIndex];
        postorderIndex--;

        TreeNode* root = new TreeNode(rootValue);
        int middle = inorderIndex[rootValue];

        root->right = build(postorder, middle + 1, right);
        root->left = build(postorder, left, middle - 1);

        return root;
    }

public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inorderIndex[inorder[i]] = i;
        }

        postorderIndex = postorder.size() - 1;

        return build(postorder, 0, inorder.size() - 1);
    }
};