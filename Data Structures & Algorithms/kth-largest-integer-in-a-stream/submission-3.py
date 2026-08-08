import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.viewIndex = k
        self.seq = nums
        heapq.heapify(self.seq)
        while len(self.seq) > k:
            heapq.heappop(self.seq)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.seq, val)
        if len(self.seq) > self.viewIndex:
            heapq.heappop(self.seq)
        return self.seq[0]
