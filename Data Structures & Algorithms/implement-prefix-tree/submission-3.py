class PrefixTree:

    def __init__(self):
        self.leaves = {} 

    def insert(self, word: str) -> None:
        curLeaves = self.leaves # Tree node pointer
        for l in word: # select leaf and insert
            if l not in curLeaves.keys():
                curLeaves[l] = {}
            curLeaves = curLeaves[l]
        curLeaves[None] = {}

    def search(self, word: str) -> bool:
        curLeaves = self.leaves
        for l in word:
            if l in curLeaves:
                curLeaves = curLeaves[l]
            else:
                return False
        if None in curLeaves:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curLeaves = self.leaves
        for l in prefix:
            if l in curLeaves.keys():
                curLeaves = curLeaves[l]
            else:
                return False
        return True
        