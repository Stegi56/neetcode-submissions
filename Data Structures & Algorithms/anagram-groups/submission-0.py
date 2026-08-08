class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = {}

        for s in strs:
            sKey = tuple(sorted(s))
            if sKey not in sortedWords.keys():
                sortedWords[sKey] = [s]
            else:
                val = sortedWords[sKey]
                val.append(s)

        return list(sortedWords.values())