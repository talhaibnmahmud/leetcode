// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    bool isSymmetric(const TreeNode* root) const {
        if (root == nullptr) return true;

        return isMirror(root->left, root->right);
    }

    bool isMirror(const TreeNode* left, const TreeNode* right) const {
        if (left == nullptr && right == nullptr) return true;
        if (left == nullptr || right == nullptr) return false;
        if (left->val != right->val) return false;

        return isMirror(left->left, right->right) && isMirror(left->right, right->left);
    }
};
