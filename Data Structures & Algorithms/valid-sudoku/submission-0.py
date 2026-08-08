class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
    # rows
    # cols
    # boxes

    #populate loop:
        # lookup right row, col, square
            # lookup helper for square
        # check for value
        # insert

        rows = {r: [] for r in range(9)}
        cols = {c: [] for c in range(9)}
        boxes = {
            "tl": [], "tm" : [], "tr" : [],
            "ml": [], "mm" : [], "mr" : [],
            "bl": [], "bm" : [], "br" : [],
        }

        def getBoxIndex(col: int, row: int) -> str:
            height = ""
            if col < 3:
                height = "t"
            elif col < 6:
                height = "m"
            elif col < 9:
                height = "b"

            side = ""
            if row < 3:
                side = "l"
            elif row < 6:
                side = "m"
            elif row < 9:
                side = "r"
            
            return (height + side)

        for col in range(9):
            for row in range(9):
                val = board[row][col]

                if val != ".":
                    if val in cols[col]:
                        return False
                    else:
                        cols[col].append(val)
            
                    if val in rows[row]:
                        return False
                    else:
                        rows[row].append(val)

                    if val in boxes[getBoxIndex(col, row)]:
                        return False
                    else:
                        boxes[getBoxIndex(col, row)].append(val)
        
        return True
            

