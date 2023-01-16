#include <array>
#include <vector>


class Solution {
private:
    bool isValid(const std::vector<char>& v) {
        std::array<bool, 9> used = {false};
        for (const auto& c : v) {
            if (c == '.') 
                continue;
            if (used[c - '1']) 
                return false;
            used[c - '1'] = true;
        }
        return true;
    }
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        for (const auto& row : board) {
            if (!isValid(row)) 
                return false;
        }

        for (auto i = 0; i < 9; i++) {
            std::vector<char> col = {};
            col.reserve(9);
            for (auto j = 0; j < 9; j++) 
                col.push_back(board[j][i]);
            
            if (!isValid(col)) 
                return false;
        }

        for (auto i = 0; i < 9; i += 3) {
            for (auto j = 0; j < 9; j += 3) {
                std::vector<char> square = {};
                square.reserve(9);
                for (auto k = 0; k < 3; ++k) {
                    for (auto l = 0; l < 3; ++l) 
                        square.push_back(board[i + k][j + l]);
                }
                if (!isValid(square)) 
                    return false;
            }
        }

        return true;
    }
};