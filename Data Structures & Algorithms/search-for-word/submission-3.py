class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #find a start point
        #recursive search neighbors with next char, add visited to stack

        path = set()
        def search(wRemainder, curi, curj):
            if not wRemainder:
                return True
            
            if curi < 0 or curi >= len(board) or curj < 0 or curj >= len(board[0]):
                return False

            if (curi, curj) in path or board[curi][curj] != wRemainder[0]:
                return False
            else:
                wRemainder = wRemainder[1:]
                path.add((curi, curj))
                res = (search(wRemainder, curi + 1, curj) or
                    search(wRemainder, curi - 1, curj) or
                    search(wRemainder, curi, curj + 1) or
                    search(wRemainder, curi, curj - 1))
                path.remove((curi,curj))
                return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if search(word, i, j):
                        return True
        return False

