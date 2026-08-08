class MedianFinder:
    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        #add val to small
        heapq.heappush(self.small, num * -1)
        #ensure balanced
        if ( self.small and self.large and 
        self.small[0] * -1 > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #fix size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((self.small[0] * - 1) + self.large[0]) / 2
           