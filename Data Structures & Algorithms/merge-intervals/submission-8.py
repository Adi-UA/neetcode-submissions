class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l,u=0,0
        res=[]
        for i,(start,end) in enumerate(intervals):
            # interval overlaps
            if intervals[l][0] <= start <= intervals[u][1]:
                if end > intervals[u][1]:
                    u=i
            # no overlap
            else:
                res.append([intervals[l][0],intervals[u][1]])
                l=u=i

        res.append([intervals[l][0],intervals[u][1]])
        return res