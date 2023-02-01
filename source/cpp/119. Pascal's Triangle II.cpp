#include <vector>


class Solution {
public:
    std::vector<int> getRow(const int& rowIndex) {
        std::vector<int> result(rowIndex + 1, 1);
        for (auto i = 1; i <= rowIndex; ++i) {
            for (auto j = i - 1; j > 0; --j) {
                result[j] += result[j - 1];
            }
        }
        return result;
    }
};
