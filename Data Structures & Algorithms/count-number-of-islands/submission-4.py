class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(row, col) -> bool:
            if (row >= len(grid) or row < 0 
                or col >= len(grid[0]) or col < 0 
                or (row, col) in visited 
                or grid[row][col] == "0"):
                    return False
            else:
                visited.add((row, col))
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row, col - 1)
                return True

        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(row, col):
                    counter += 1
        
        return counter