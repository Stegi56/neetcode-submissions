class Trie:
    def __init__(self):
        self.isWord = False
        self.word = ""
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #build trie
        #search function
        #iterate through board, use dfs
        root = Trie()

        for word in words:
            cur = root
            for char in word:
                if char not in cur.children.keys():
                    cur.children[char] = Trie()
                cur = cur.children[char]
            cur.isWord = True
            cur.word = word
        
        res = set()
        def getNode(char, trieP) -> Optional[Trie]:
            if char in trieP.children.keys():
                next = trieP.children[char]
                if next.isWord:
                    res.add(next.word)
                return next
            else:
                return None

        visited = set()
        def dfs(i, j, prev):
            if not (i >= 0 and i < len(board) and j >= 0 and j < len(board[0])):
                return
            
            if (i,j) not in visited:
                cur = getNode(board[i][j], prev)
                if cur:
                    visited.add((i,j))
                    dfs(i + 1, j, cur)
                    dfs(i - 1, j, cur)
                    dfs(i, j + 1, cur)
                    dfs(i, j - 1, cur)
                    visited.remove((i,j))
                return
            else:
                return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return list(res)

