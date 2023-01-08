function matrixReshape(mat: number[][], r: number, c: number): number[][] {
    const rows = mat.length;
    const cols = mat[0].length;

    if (rows * cols != r * c)
        return mat;

    const result: number[][] = new Array(r).fill(0).map(() => new Array(c).fill(0));

    for (let i = 0; i < rows * cols; i++) {
        result[Math.floor(i / c)][i % c] = mat[Math.floor(i / cols)][i % cols];
    }

    return result;
};