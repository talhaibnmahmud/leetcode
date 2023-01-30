#include <algorithm>
#include <queue>


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
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;

        TreeNode* left = invertTree(root->left);
        TreeNode* right = invertTree(root->right);

        std::swap(root->left, root->right);
        return root;
    }

    // TreeNode* invertTree(TreeNode* root) {
    //     if (root == nullptr) return nullptr;

    //     std::queue<TreeNode*> q;
    //     q.push(root);

    //     while (!q.empty()) {
    //         TreeNode* node = q.front();
    //         q.pop();

    //         std::swap(node->left, node->right);

    //         if (node->left != nullptr) q.push(node->left);
    //         if (node->right != nullptr) q.push(node->right);
    //     }

    //     return root;
    // }
};
