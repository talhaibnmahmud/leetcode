import math


class Solution:
    def __init__(self):
        self.fuel = 0

    def dfs(self, node: int, parent: int, adj: list[list[int]], seats: int) -> int:
        # The node itself has one representative.
        representatives = 1
        for child in adj[node]:
            if child == parent:
                continue

            # Add count of representatives in each child subtree to the parent subtree.
            representatives += self.dfs(child, node, adj, seats)

        if node != 0:
            # Count the fuel it takes to move to the parent node.
            # Root node does not have any parent so we ignore it.
            self.fuel += math.ceil(representatives / seats)

        return representatives

    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        self.fuel = 0

        n = len(roads) + 1
        adj: list[list[int]] = [[] for _ in range(n)]

        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])

        self.dfs(0, -1, adj, seats)

        return self.fuel


def test():
    s = Solution()

    roads = [[0, 1], [0, 2], [0, 3]]
    seats = 5
    assert s.minimumFuelCost(roads, seats) == 3

    roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
    seats = 2
    assert s.minimumFuelCost(roads, seats) == 7

    assert s.minimumFuelCost([], 1) == 0

    print("All tests passed!")


if __name__ == '__main__':
    test()
