class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = defaultdict(list)

        for s in strs:
            sKey = [0] * 26

            for char in s:
                sKey[ord(char) - ord("a")] += 1

            sKey = tuple(sKey)
            sortedWords[sKey].append(s)

        return list(sortedWords.values())