class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # approach: go through intervals
        # 1) no overlap - newInterval end before interval[i] start > append 
        #    newInterval to res and return res + intervals[i:]
        # 2) no overlap - newInterval start after interval[i] end > append 
        #    interval[i] to res
        # 3) overlap - newInterval start before interval[i] end > merge newInterval 
        intervals.sort()
        res=[]

        for i, (start,end) in enumerate(intervals):
            if newInterval[1] < start: 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end: 
                res.append(intervals[i])
            else: 
                newInterval=[min(start,newInterval[0]),max(end,newInterval[1])]
        res.append(newInterval)
        return res
