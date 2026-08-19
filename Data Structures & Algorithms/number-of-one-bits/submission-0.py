class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for b in bin(n):
            if b == "1": 
                counter += 1
        return counter