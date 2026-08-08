class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        # add letters with counters to hasmap
        # subtract
        # if empty return true

        myMap = {}

        for l in s:
            if l not in myMap:
                myMap[l] = 1
            else:
                myMap[l] += 1

        for l in t:
            if l not in myMap:
                return False
            elif myMap[l] >= 1:
                myMap[l] -= 1
            else:
                return False
        
        return not sum(myMap.values()) > 0