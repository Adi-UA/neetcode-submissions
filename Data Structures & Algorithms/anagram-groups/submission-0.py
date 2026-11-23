class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary then grab values (keys are sorted tuples)
        d={}
        for s in strs:
            tup=tuple(sorted(list(s)))
            if tup not in d:
                d[tup]=[]
            d[tup].append(s)
        res=[]
        for _,v in d.items():
            res.append(v)
        return res