class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCounter = defaultdict(int)

        for n in nums:
            elementCounter[n] += 1

        elementCounter = dict(
            sorted(
                elementCounter.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
        
        res = []
        for key in elementCounter:
            if len(res) == k:
                break
            res.append(key)

        return res