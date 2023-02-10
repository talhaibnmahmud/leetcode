from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        # BFS
        # Time: O(n^2), Space: O(n^2)
        n = len(grid)
        q: deque[tuple[int, int]] = deque()

        # Add all the land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        # If all the cells are land or all the cells are water, return -1
        if len(q) == 0 or len(q) == n * n:
            return -1

        # Initialize the distance to -1
        dist = -1
        # Iterate until through all the land cells
        while q:
            dist += 1
            # Iterate through all the land cells in the current level
            for _ in range(len(q)):
                i, j = q.popleft()
                # Check all the adjacent cells (up, down, left, right --> Manhattan distance)
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    # If the adjacent cell is water, mark it as visited and add it to the queue
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y))

        return dist


def test():
    s = Solution()

    assert s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert s.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4

    print("All tests passed!")


if __name__ == "__main__":
    test()
