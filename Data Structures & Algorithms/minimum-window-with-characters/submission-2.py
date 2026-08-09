class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # slide window
        # if does not contain move right
        # if contains move left, max(cur, res)
        window = defaultdict(int)
        tMap = defaultdict(int)
        for c in t:
            tMap[c] += 1

        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(tMap.keys())
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if resLen > ((r - l) + 1):
                    res, resLen = [l, r], ((r - l) + 1)

                if window[s[l]] == tMap[s[l]]:
                    have -= 1
                
                window[s[l]] -= 1
                l += 1
            
        
        return s[res[0]: res[1] + 1] if resLen != float("inf") else ""

                


            