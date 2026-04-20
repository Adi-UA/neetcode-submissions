import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort arr
        piles.sort()

        # binary search for k: between 1 and largest pile size
        l,r = 1, piles[-1]
        min_k = 0
        while l <= r:
            # set k
            k = (l+r)//2
            print(f"k:{k}")
            # count no hours needed
            hours = 0
            for b in piles:
                hours += math.ceil(b/k)
                print(hours)
                if hours > h: # if k rate too slow, move l up
                    l = k + 1
                    break # stop checking when exceeds time
            if hours <= h: # if k too fast, move r down
                min_k = k # track k
                print(min_k)
                r = k - 1
        return min_k