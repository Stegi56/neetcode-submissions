"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        times = defaultdict(int)

        for i in intervals:
            times[i.start] += 1
            times[i.end] -= 1

        prev = 0
        res = 0
        for t in sorted(times.keys()):
            prev += times[t]
            res = max(res, prev)

        return res
        