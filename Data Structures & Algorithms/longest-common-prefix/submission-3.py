class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pointer = 0
        cur = ""
        while True:
            for s in strs:
                if pointer >= len(s):
                    return s[:pointer]
                elif cur == "":
                    cur = s[pointer]
                elif s[pointer] != cur:
                    return s[:pointer]
            cur = ""
            pointer += 1