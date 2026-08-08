class Solution:

    def encode(self, strs: List[str]) -> str:
        # 3,5,34:strstrstr
        #
        # generate sepperator indexes
        # generate sepperator string + ":" + mergedStrs
        if not strs:
            return ":"

        sepperators = ""
        mergedStr = ""
        for s in strs:
            if len(sepperators) > 0:
                sepperators += ","
            sepperators += str(len(s))
            mergedStr += s
        
        return sepperators + ":" + mergedStr

    def decode(self, s: str) -> List[str]:
       #read string left to right
       #as we read build sepperators
       #on first : switch to res build mode and use sepperator counting
        if s == ":":
            return []

        mode = "sepperator" 

        sepperator = ""
        sepperators = []

        res = []
        buildString = ""
        counter = 0
        for char in s:
            if mode == "sepperator":
                if char == ":":
                    sepperators.append(int(sepperator))
                    mode = "build"
                    counter = sepperators[0]
                    del sepperators[0] 
                elif char == ",":
                    sepperators.append(int(sepperator))
                    sepperator = ""
                else: sepperator += char
            elif mode == "build":
                if counter > 0:
                    buildString += char
                    counter -= 1
                else:
                    res.append(buildString)
                    buildString = char
                    while sepperators[0] == 0:
                        res.append("")
                        del sepperators[0] 
                    counter = sepperators[0] - 1
                    del sepperators[0] 

        res.append(buildString)
        while sepperators and sepperators[0] == 0:
            res.append("")
            del sepperators[0] 
        return res