class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l,u=0,0
        res=[]
        for i in range(len(intervals)):
            # interval overlaps
            if intervals[l][0] <= intervals[i][0] <= intervals[u][1]:
                if intervals[i][1] > intervals[u][1]:
                    u=i
            # no overlap
            else:
                res.append([intervals[l][0],intervals[u][1]])
                l=u=i

        res.append([intervals[l][0],intervals[u][1]])
        return res