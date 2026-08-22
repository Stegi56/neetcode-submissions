class TreeNode:
    def __init__(self):
        self.isWord = False
        self.leaves = defaultdict(lambda: TreeNode())

class WordDictionary:
    def __init__(self):
        self.base = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.base
        for c in word:
            cur = cur.leaves[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(p, node) -> bool:
            if p >= len(word):
                return node.isWord
            elif word[p] != "." and word[p] in node.leaves:
                return dfs(p + 1, node.leaves[word[p]])
            elif word[p] == "." and node.leaves:
                res = False
                for leafNode in node.leaves.values():
                    res = res or dfs(p + 1, leafNode)
                return res
            else:
                return False
        
        return dfs(0, self.base)

                