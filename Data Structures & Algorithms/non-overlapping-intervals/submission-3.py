class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # approach: sort first, then track the prevEnd, if curr start is before
        # then it's an overlap. If overlap, keep the prevEnd that is shorter
        intervals.sort()

        res=0
        if not intervals:
            return res
        prevEnd=intervals[0][1]
        for (start,end) in intervals[1:]:
            # overlap
            if start < prevEnd:
                res+=1
                prevEnd=min(prevEnd,end)
            else: # not overlap
                prevEnd=end
        return res