class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCounter = defaultdict(int)

        for n in nums:
            elementCounter[n] += 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, frequency in elementCounter.items():
            buckets[frequency].append(num)

        res = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
