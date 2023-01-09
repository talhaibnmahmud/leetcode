class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        result = [[1]]

        for i in range(1, numRows):
            result.append([1] + [result[i-1][j] + result[i-1][j+1]
                          for j in range(i-1)] + [1])

        return result
