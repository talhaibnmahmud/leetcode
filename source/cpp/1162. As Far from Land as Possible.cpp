#include <queue>
#include <vector>


class Solution {
public:
    int maxDistance(std::vector<std::vector<int>>& grid) const {
        if (grid.size() == 1) return -1;

        std::queue<std::pair<int, int>> q;
        for (auto i = 0; i < grid.size(); ++i) {
            for (auto j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j] == 1)
                    q.push({ i, j });
            }
        }

        if (q.size() == 0 || q.size() == grid.size() * grid[0].size()) return -1;

        int maxDistance = 0;
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();

            if (i > 0 && grid[i - 1][j] == 0) {
                grid[i - 1][j] = grid[i][j] + 1;
                q.push({ i - 1, j });
            }
            if (i < grid.size() - 1 && grid[i + 1][j] == 0) {
                grid[i + 1][j] = grid[i][j] + 1;
                q.push({ i + 1, j });
            }
            if (j > 0 && grid[i][j - 1] == 0) {
                grid[i][j - 1] = grid[i][j] + 1;
                q.push({ i, j - 1 });
            }
            if (j < grid[i].size() - 1 && grid[i][j + 1] == 0) {
                grid[i][j + 1] = grid[i][j] + 1;
                q.push({ i, j + 1 });
            }

            maxDistance = std::max(maxDistance, grid[i][j] - 1);
        }

        return maxDistance;
    }
};
