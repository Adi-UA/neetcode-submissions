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
        # 2. (prev) Get left pointer after loop if no timestamp
        # 3. "" else if left pointer larger than timestamp
        targetVals = self._timeMap.get(key,None)
        if targetVals is None: 
            return "" # takes care of when key doesn't exist
        print(f"getting new value from {targetVals}")
        l, r = 0, len(targetVals) - 1
        while l <= r:
            m = (l+r) // 2
            currStamp = targetVals[m][0]
            currVal = targetVals[m][1]
            if currStamp == timestamp:
                return currVal
            elif currStamp < timestamp:
                l = m + 1
            else:
                r = m - 1
        # get prev stamp if it is less than target stamp
        print(l,r)
        if targetVals[min(l,r)][0] < timestamp:
            return targetVals[min(l,r)][1]
        else:
            return ""
