#include <vector>


class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        const auto n = matrix[0].size() - 1;
        for (auto& row : matrix) {
            if (row[n] < target) continue;

            for (auto& col : row) 
                if (col == target) return true;
        }

        return false;
    }
};