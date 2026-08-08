from collections import deque
class PrefixTree:

    def __init__(self):
        self.value = None
        self.nextTs = []

    def insert(self, word: str) -> None:
        
        # extract letter
        qWord = deque(word)
        l = qWord.popleft() if qWord else None

        
        exists = False
        for t in self.nextTs: # select leaf and insert
            if t.value == l:
                exists = True
                if l:
                    t.insert("".join(qWord)) # continue insertion if not end of word (None)
                else:
                    break
        
        if not exists: # create leaf and insert
            newLeaf = PrefixTree()
            newLeaf.value = l
            if l: 
                newLeaf.insert("".join(qWord)) # continue insertion if not end of word (None)
            self.nextTs.append(newLeaf)


    def search(self, word: str) -> bool:
        qWord = deque(word)
        l = qWord.popleft() if qWord else None # extract letter
        for t in self.nextTs:
            if t.value == l:
                if l: # continue search if not end of word (None letter)
                    return t.search("".join(qWord))
                else:
                    return True
        return False
                


    def startsWith(self, prefix: str) -> bool:
        qWord = deque(prefix)
        if not qWord:
            return True
        l = qWord.popleft() # extract letter
        for t in self.nextTs:
            if t.value == l:
                return t.startsWith("".join(qWord))
        return False
        