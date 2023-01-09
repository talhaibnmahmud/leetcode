#include <cassert>
#include <iostream>
#include <vector>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> result;
        if (numRows == 0) 
            return result;
        
        result.reserve(numRows);
        
        result.push_back({1});
        for (int i = 1; i < numRows; i++) {
            std::vector<int> row;
            row.reserve(i + 1);

            row.push_back(1);
            for (int j = 1; j < i; j++) 
                row.push_back(result[i - 1][j - 1] + result[i - 1][j]);
            
            row.push_back(1);

            result.push_back(row);
        }

        return result;
    }
};


int main() {
    Solution s;

    auto result = s.generate(5);
    assertm(result.size() == 5, "Wrong size");
    assertm(result[0].size() == 1, "Wrong size");
    assertm(result[1].size() == 2, "Wrong size");
    assertm(result[2].size() == 3, "Wrong size");
    assertm(result[3].size() == 4, "Wrong size");
    assertm(result[4].size() == 5, "Wrong size");

    assertm(result[0][0] == 1, "Wrong value");
    assertm(result[1][0] == 1, "Wrong value");
    assertm(result[1][1] == 1, "Wrong value");
    assertm(result[2][0] == 1, "Wrong value");
    assertm(result[2][1] == 2, "Wrong value");
    assertm(result[2][2] == 1, "Wrong value");
    assertm(result[3][0] == 1, "Wrong value");
    assertm(result[3][1] == 3, "Wrong value");
    assertm(result[3][2] == 3, "Wrong value");
    assertm(result[3][3] == 1, "Wrong value");
    assertm(result[4][0] == 1, "Wrong value");
    assertm(result[4][1] == 4, "Wrong value");
    assertm(result[4][2] == 6, "Wrong value");
    assertm(result[4][3] == 4, "Wrong value");
    assertm(result[4][4] == 1, "Wrong value");

    std::cout << "All tests passed!" << std::endl;
    return 0;
}
