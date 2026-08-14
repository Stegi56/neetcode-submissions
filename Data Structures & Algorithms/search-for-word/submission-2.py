class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #find a start point
        #recursive search neighbors with next char, add visited to stack

        def search(wRemainder, curi, curj, visitedCells):
            if not wRemainder:
                return True
            
            if curi < 0 or curi >= len(board) or curj < 0 or curj >= len(board[0]):
                return False

            if (curi, curj) in visitedCells or board[curi][curj] != wRemainder[0]:
                return False
            else:
                newV = visitedCells.union({(curi, curj)})
                wRemainder = wRemainder[1:]
                return (search(wRemainder, curi + 1, curj, newV) or
                    search(wRemainder, curi - 1, curj, newV) or
                    search(wRemainder, curi, curj + 1, newV) or
                    search(wRemainder, curi, curj - 1, newV))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if search(word, i, j, set()):
                        return True
        return False

