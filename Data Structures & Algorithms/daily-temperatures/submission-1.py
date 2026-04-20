class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while len(s) > 0:
                top_i, top_t = s[-1]
                if temp > top_t:
                    res[top_i] = i - top_i
                    s.pop()
                else:
                    break
            s.append((i,temp))
        return res
        