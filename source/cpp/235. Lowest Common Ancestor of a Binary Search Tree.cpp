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
    TreeNode* lowestCommonAncestor(TreeNode* root, const TreeNode* p, const TreeNode* q) const {
        std::queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();
            
            if (node->val > p->val && node->val > q->val) queue.push(node->left);
            else if (node->val < p->val && node->val < q->val) queue.push(node->right);
            else return node;
        }

        return nullptr;
    }
};
