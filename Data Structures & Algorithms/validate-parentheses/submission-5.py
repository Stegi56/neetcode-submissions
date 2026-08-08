from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        def inverse(c):
            if c == "(":
                return ")"
            if c == "{":
                return "}"
            if c == "[":
                return "]"

        def toPush(c):
            if (c =="(") or (c == "{") or (c == "["):
                return True
            else:
                return False

        myStack = deque()

        for c in s:
            if toPush(c):
                myStack.append(c)
            elif len(myStack) == 0:
                return False
            elif inverse(myStack.pop()) != c:
                return False
        if len(myStack) == 0:
            return True
        else:
            return False
        