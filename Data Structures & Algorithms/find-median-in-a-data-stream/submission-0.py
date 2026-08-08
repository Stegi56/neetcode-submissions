from collections import heapq
class MedianFinder:
    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        self.values.append(num)
        self.values.sort()

    def findMedian(self) -> float:
        if (len(self.values) % 2 == 1):
            return self.values[len(self.values) // 2]
        else:
            upper = self.values[len(self.values) // 2]
            lower = self.values[(len(self.values) // 2) - 1]
            return (upper + lower) / 2