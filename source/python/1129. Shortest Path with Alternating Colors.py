from queue import Queue


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        if n == 1:
            return [0]

        # Create adjacency lists for red and blue edges
        red: list[list[int]] = [[] for _ in range(n)]
        blue: list[list[int]] = [[] for _ in range(n)]

        # Initialize the adjacency lists
        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        # Initialize the queue and put the starting node in it
        q: Queue[tuple[int, str, int]] = Queue()
        q.put((0, 'r', 0))
        q.put((0, 'b', 0))

        # Initialize the visited set and put the starting node in it
        visited: set[tuple[int, str]] = set()
        visited.add((0, 'r'))
        visited.add((0, 'b'))

        # Create the answer array and initialize the first element
        ans = [-1] * n
        ans[0] = 0

        # Traverse the graph
        while not q.empty():
            u, color, d = q.get()

            # If the current color is red, traverse the blue edges, and vice versa
            if color == 'r':
                for v in red[u]:
                    # If the node has already been visited with the opposite color, continue
                    if (v, 'b') in visited:
                        continue

                    # If the node has not been visited, add it to the visited set and the queue
                    visited.add((v, 'b'))
                    q.put((v, 'b', d + 1))

                    # If the node has not been visited before, update the answer array
                    if ans[v] == -1:
                        ans[v] = d + 1
            else:
                for v in blue[u]:
                    if (v, 'r') in visited:
                        continue

                    visited.add((v, 'r'))
                    q.put((v, 'r', d + 1))

                    if ans[v] == -1:
                        ans[v] = d + 1

        return ans


def test():
    s = Solution()

    assert s.shortestAlternatingPaths(
        3, [[0, 1], [1, 2]], [[1, 0]]
    ) == [0, 1, -1]
    assert s.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]) == [0, 1, -1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
