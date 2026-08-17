class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        res = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= cur[1]: #continue if no overlap based on no -> <-overlap
                res.append(cur)
                cur = intervals[i]
                continue
            elif intervals[i][1] > cur[1]: # if overlapping remove interval that has greater -> ->
                continue
            else:
                cur = intervals[i]
        res.append(cur)
        return len(intervals) - len(res)
