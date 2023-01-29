#include <stack>
#include <vector>


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
    std::vector<int> preorderTraversal(const TreeNode* root) const {
        if (root == nullptr) return {};

        std::vector<int> result;
        std::stack<const TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            auto node = stack.top();
            stack.pop();
            result.push_back(node->val);

            if (node->right != nullptr) stack.push(node->right);
            if (node->left != nullptr) stack.push(node->left);
        }

        return result;
    }

    std::vector<int> ans;
    void preorder(const TreeNode* root) {
        if(root==nullptr) return;

        ans.push_back(root->val);
        preorder(root->left);
        preorder(root->right);
    }
    std::vector<int> preorderTraversal(const TreeNode* root) {
        //root left right
        preorder(root);
        return ans;
    }
};
