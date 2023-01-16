from bisect import bisect_left
from queue import LifoQueue


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        # Find the index of the first interval that starts after the new interval
        index = bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)

        # Merge intervals
        stack: LifoQueue[list[int]] = LifoQueue()

        for start, end in intervals:
            if not stack.empty() and stack.queue[-1][1] >= start:
                prev_start, prev_end = stack.get()
                stack.put([prev_start, max(prev_end, end)])
            else:
                stack.put([start, end])

        return list(stack.queue)


def test():
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [
                    4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [5, 7]) == [[5, 7]]
    assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert s.insert([[1, 5]], [2, 7]) == [[1, 7]]

    # Edge cases
    assert s.insert([[3, 5], [12, 15]], [6, 6]) == [[3, 5], [6, 6], [12, 15]]

    print("All tests passed.")


if __name__ == "__main__":
    test()
