class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(rows * cols):
            result[i // c][i % c] = mat[i // cols][i % cols]

        return result
