class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for _ in matrix[0]] for _ in matrix]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                upper = 0
                if row >= 1:
                    upper = self.prefix[row - 1][col]
                
                prev = 0
                if col >= 1:
                    prev = self.prefix[row][col - 1]

                duplicate = 0
                if row >= 1 and col >= 1:
                    duplicate = self.prefix[row - 1][col - 1]

                cur = matrix[row][col]

                self.prefix[row][col] = upper + prev - duplicate + cur

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        overshot = self.prefix[row2][col2]
        upper = 0
        if (row1 - 1) >= 0:
            upper = self.prefix[row1 - 1][col2]
        
        lower = 0
        if (col1 -1) >= 0:
            lower = self.prefix[row2][col1 - 1]

        duplicate = 0
        if row1 > 0 and col1 > 0:
            duplicate = self.prefix[row1 - 1][col1 - 1]
        
        return overshot - upper - lower + duplicate


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)