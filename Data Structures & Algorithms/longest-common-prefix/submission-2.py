class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        pointer = 0
        cur = ""
        while True:
            for s in strs:
                if pointer >= len(s):
                    return res
                elif cur == "":
                    cur = s[pointer]
                elif s[pointer] != cur:
                    return res
            res = res + cur
            cur = ""
            pointer += 1