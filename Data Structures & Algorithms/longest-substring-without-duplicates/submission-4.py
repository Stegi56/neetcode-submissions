from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = deque()
        for l in range(len(s)):
            while s[l] in window:
                window.popleft()
            window.append(s[l])
            longest = max(longest, len(window))
        return longest