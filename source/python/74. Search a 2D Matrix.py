class Solution:
    # def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    #     if not matrix:
    #         return False

    #     m, n = len(matrix), len(matrix[0])
    #     row, col = 0, 0

    #     if n == 1:
    #         return target in [matrix[i][0] for i in range(m)]

    #     while row < m:
    #         if matrix[row][0] <= target <= matrix[row][n - 1]:
    #             break
    #         row += 1

    #     if row == m:
    #         return False

    #     while col < n:
    #         if matrix[row][col] == target:
    #             return True
    #         col += 1

    #     return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False


def test():
    s = Solution()
    assert s.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    ) == True
    assert s.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    ) == False
    assert s.searchMatrix(matrix=[], target=0) == False

    # Failed in attempt 1
    assert s.searchMatrix(
        matrix=[[1], [3]], target=3
    ) == True
    assert s.searchMatrix(
        matrix=[[1, 1], [2, 2]], target=2
    ) == True

    print("All tests passed!")


if __name__ == "__main__":
    test()
