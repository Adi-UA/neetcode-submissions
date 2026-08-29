"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts=sorted([i.start for i in intervals])
        ends=sorted([i.end for i in intervals])
        res,count=0,0
        si,ei=0,0
        while si<len(starts):
            # overlap
            if starts[si] < ends[ei]:
                count+=1
                si+=1
                res=max(res,count)
            else:
                count-=1
                ei+=1
        return res
