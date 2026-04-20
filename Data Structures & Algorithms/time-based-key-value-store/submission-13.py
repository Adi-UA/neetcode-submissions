class TimeMap:

    def __init__(self):
        # format: timeMap = {"alice" = [(1,"happy"), (3, "sad")], ...}
        self._timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add new key or update values into key with tuple (timeStamp, value)
        if self._timeMap.get(key) is None:
            self._timeMap[key] = []
        self._timeMap[key].append( (timestamp, value) )
        print(f"updating timemap as: {self._timeMap}")
        

    def get(self, key: str, timestamp: int) -> str:
        # 1. Binary search for timestamp in dict
        # 2. l always going to get closest on left (prev stamp) to target stamp except at end
        #.   so save val before updating l.
        # 3. default is "" if no val matching
        res = ""
        targetVals = self._timeMap.get(key,[])
        l, r = 0, len(targetVals) - 1
        while l <= r:
            m = (l+r) // 2
            currStamp = targetVals[m][0]
            currVal = targetVals[m][1]
            
            if currStamp <= timestamp:
                res = currVal
                l = m + 1
            else:
                r = m - 1
        return res
