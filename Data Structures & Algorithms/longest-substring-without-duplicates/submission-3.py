from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = deque()
        for l in range(len(s)):
            if s[l] not in window:
                window.append(s[l])
                longest = max(longest, len(window))
            else:
                while s[l] in window:
                    window.popleft()
                window.append(s[l])
        
        return longest