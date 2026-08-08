class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitisedString = []
        for l in s:
            if l.isalnum():
                sanitisedString.append(l.lower())

        for i in range(len(sanitisedString)):
            if i <= (len(sanitisedString)//2 + 1):
                if sanitisedString[i] != sanitisedString[-i - 1]:
                    return False
            else:
                return True
        return True