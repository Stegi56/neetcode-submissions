class MedianFinder:
    def __init__(self):
        self.small = [] #maxheap -ves
        self.large = [] #minheap +ves

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        #check correct
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            heapq.heappush(self.large,
                heapq.heappop(self.small) * -1
            )

        #balance
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large,
                heapq.heappop(self.small) * -1
            )

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small,
                heapq.heappop(self.large) * -1
            )

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return ((self.small[0] * -1) + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        else:
            return self.large[0]