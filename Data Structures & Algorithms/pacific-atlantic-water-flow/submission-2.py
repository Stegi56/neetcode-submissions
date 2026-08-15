class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # brute force
        # check all start points
        # do a dfs search in all four directions

        #visited = set()
        #canDoBoth = set()
        #def canAccessPacific(i, j, prevVal) -> bool:
        #    if i < 0 or j < 0:
        #        return True
        #    if i >= len(heights) or j >= len(heights[0]) or (i, j) in visited:
        #        return False
#
        #    curVal = heights[i][j]    
        #    if not (curVal <= prevVal):
        #        return False
#
        #    if (i, j) in canDoBoth:
        #        return True
#
        #    visited.add((i, j))
        #    cap = (
        #        canAccessPacific(i + 1, j, curVal) or
        #        canAccessPacific(i - 1, j, curVal) or
        #        canAccessPacific(i, j + 1, curVal) or
        #        canAccessPacific(i, j - 1, curVal)
        #    )
        #    visited.remove((i,j))
        #    return cap
#
        #def canAccessAtlantic(i, j, prevVal) -> bool:
        #    if i < 0 or j < 0 or (i, j) in visited:
        #        return False
        #    if i >= len(heights) or j >= len(heights[0]):
        #        return True
#
        #    curVal = heights[i][j]    
        #    if not (curVal <= prevVal):
        #        return False
#
        #    if (i, j) in canDoBoth:
        #        return True
#
        #    visited.add((i, j))
        #    caa = (
        #        canAccessAtlantic(i + 1, j, curVal) or
        #        canAccessAtlantic(i - 1, j, curVal) or
        #        canAccessAtlantic(i, j + 1, curVal) or
        #        canAccessAtlantic(i, j - 1, curVal)
        #    )
        #    visited.remove((i,j))
        #    return caa
#
        #for i in range(len(heights)):
        #    for j in range(len(heights[0])):
        #        if canAccessPacific(i, j, float("inf")) and canAccessAtlantic(i, j, float("inf")):
        #            canDoBoth.add((i, j))
#
        #res = list(canDoBoth)
        #for index, pair in enumerate(res):
        #    res[index] = [res[index][0], res[index][1]]
#
        #return res

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = list(pac & atl)

        for index, coords in enumerate(res):
            res[index] = [coords[0], coords[1]]

        return res
