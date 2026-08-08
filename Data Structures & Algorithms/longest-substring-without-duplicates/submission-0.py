class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for l in range(len(s)):
            hashSet = set()
            for r in range(l,len(s)):
                if s[r] not in hashSet:
                    hashSet.add(s[r])
                else:
                    break
            longest = max(longest, len(hashSet))
        
        return longest