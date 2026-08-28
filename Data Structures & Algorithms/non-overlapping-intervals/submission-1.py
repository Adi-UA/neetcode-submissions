class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # approach: sort first, then grab nonoverlapping intervals and subtract
        # length with original length
        intervals.sort()

        res_list=[]
        for i,(start,end) in enumerate(intervals):
            last_i=len(res_list)-1
            if not res_list:
                res_list.append(intervals[i])
            elif intervals[i][0] < res_list[last_i][1]:
                # if overlap with previous, and the newer
                # one ends earlier, replace
                if intervals[i][1] < res_list[last_i][1]:
                    res_list[last_i]=intervals[i]
            else: # no overlap
                res_list.append(intervals[i])
        return len(intervals)-len(res_list)