#include <queue>
#include <vector>


class Solution {
public:
    std::vector<int> shortestAlternatingPaths(
        const int& n, std::vector<std::vector<int>>& redEdges, std::vector<std::vector<int>>& blueEdges) {
        std::vector<std::vector<std::pair<int, int>>> adj(n);
        for (auto& redEdge : redEdges) adj[redEdge[0]].push_back({redEdge[1], 0});
        for (auto& blueEdge : blueEdges) adj[blueEdge[0]].push_back(std::make_pair(blueEdge[1], 1));

        std::vector<int> answer(n, -1);
        std::vector<std::vector<bool>> visit(n, std::vector<bool>(2));
        std::queue<std::tuple<int, int, int>> q;

        // Start with node 0, with number of steps as 0 and undefined color -1.
        q.push({0, 0, -1});
        visit[0][1] = visit[0][0] = true;
        answer[0] = 0;

        while (!q.empty()) {
            const auto [node, steps, prevColor] = q.front();
            q.pop();

            for (const auto& [neighbor, color] : adj[node]) {
                if (color == prevColor || visit[neighbor][color] == true) continue;
                
                visit[neighbor][color] = true;
                q.push({neighbor, 1 + steps, color});
                if (answer[neighbor] == -1) answer[neighbor] = 1 + steps;
            }
        }

        return answer;
    }
};
