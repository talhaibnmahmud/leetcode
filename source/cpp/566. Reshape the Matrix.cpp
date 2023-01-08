#include <cassert>
#include <iostream>
#include <vector>


// uncomment to disable assert()
// #define NDEBUG

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))


class Solution {
public:
    std::vector<std::vector<int>> matrixReshape(std::vector<std::vector<int>>& mat, int r, int c) {
        int rows = mat.size();
        int cols = mat[0].size();

        if (rows * cols != r * c)
            return mat;

        std::vector<std::vector<int>> result(r, std::vector<int>(c));

        for (int i = 0; i < rows * cols; i++)
            result[i / c][i % c] = mat[i / cols][i % cols];

        return result;
    }
};


int main()
{
    Solution solution;

    std::vector<std::vector<int>> mat{ { 1, 2 }, { 3, 4 } };
    int r = 1;
    int c = 4;

    std::vector<std::vector<int>> result = solution.matrixReshape(mat, r, c);

    assertm(result.size() == 1, "Result size is not 1.");
    assertm(result[0].size() == 4, "Result[0] size is not 4.");
    assertm(result[0][0] == 1, "Result[0][0] is not 1.");
    assertm(result[0][1] == 2, "Result[0][1] is not 2.");
    assertm(result[0][2] == 3, "Result[0][2] is not 3.");
    assertm(result[0][3] == 4, "Result[0][3] is not 4.");

    std::cout << "All tests passed." << std::endl;

    return 0;
}
