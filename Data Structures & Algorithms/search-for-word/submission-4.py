class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #find a start point
        #recursive search neighbors with next char, add visited to stack

        path = set()
        def search(wPointer, curi, curj):
            if not wPointer < len(word):
                return True
            
            if curi < 0 or curi >= len(board) or curj < 0 or curj >= len(board[0]):
                return False

            if (curi, curj) in path or board[curi][curj] != word[wPointer]:
                return False
            else:
                path.add((curi, curj))
                wPointer += 1
                res = (search(wPointer, curi + 1, curj) or
                    search(wPointer, curi - 1, curj) or
                    search(wPointer, curi, curj + 1) or
                    search(wPointer, curi, curj - 1))
                path.remove((curi,curj))
                return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if search(0, i, j):
                        return True
        return False

