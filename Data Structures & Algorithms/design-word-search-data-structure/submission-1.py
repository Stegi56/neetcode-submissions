class TreeNode:
    def __init__(self):
        self.word = False
        self.leaves = {}

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()
        #track each layer

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.leaves.keys():
                cur.leaves[char] = TreeNode()
            cur = cur.leaves[char]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            for i in range(i, len(word)):
                c = word[i]

                if c == ".":
                    for c in node.leaves.values():
                        if dfs(i + 1, c):
                            return True
                    return False
                else:
                    if c not in node.leaves.keys():
                        return False
                    node = node.leaves[c]
            return node.word

        return dfs(0, self.root)