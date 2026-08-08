class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(i, j):
            if (grid[i][j] == "1") and ((i,j) not in visited):
                visited.add((i,j))
                toCheck = [
                    [i+1, j], [i-1, j], [i, j+1], [i, j-1]
                ]
                for ci, cj in toCheck:
                    if (ci in range(rows)) and (cj in range(cols)):
                        dfs(ci, cj)

        def bfs(i,j):
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))

            while q:
                row, col = q.popleft()
                toCheck = [
                    [row+1, col], [row-1, col], [row, col+1], [row, col-1]
                ]
                for ci, cj in toCheck:
                    if (ci in range(rows)) and (cj in range(cols)) and ((ci,cj) not in visited) and (grid[ci][cj] == "1"):
                        q.append((ci,cj))
                        visited.add((ci,cj))

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == "1") and ((i,j) not in visited):
                    bfs(i, j)
                    islands += 1

        return islands
        