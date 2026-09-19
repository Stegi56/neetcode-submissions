class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                upper = self.prefix[row][col + 1]
                prev = self.prefix[row + 1][col]
                duplicate = self.prefix[row][col]
                cur = matrix[row][col]

                self.prefix[row + 1][col + 1] = upper + prev - duplicate + cur

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        overshot = self.prefix[row2 + 1][col2 + 1]
        upper = self.prefix[row1][col2 + 1]
        lower = self.prefix[row2 + 1][col1]
        duplicate = self.prefix[row1][col1]
        
        return overshot - upper - lower + duplicate


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)