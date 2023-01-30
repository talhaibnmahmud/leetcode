#include <climits>
#include <unordered_set>


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
    bool findTarget(const TreeNode* root, const int& k) const {
        std::unordered_set<int> set;
        return findTarget(root, k, set);
    }

    bool findTarget(const TreeNode* root, const int& k, std::unordered_set<int>& set) const {
        if (root == nullptr) return false;
        if (set.find(k - root->val) != set.end()) return true;
        
        set.insert(root->val);
        return findTarget(root->left, k, set) || findTarget(root->right, k, set);
    }
};