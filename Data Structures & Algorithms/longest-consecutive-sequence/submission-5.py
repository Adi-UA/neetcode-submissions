class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums to a set
        # create a lengthMap {start:length}
        # while loop and pop items per iteration
        # each iter: add to lengthMap and look for next num in set or lengthmap until you can't find consecutivs
            # if in set, delete from set and add 1 to length, if in lengthMap, add the value to this key's val
        numsSet=set(nums)
        lengthMap={}
        longest=0
        while numsSet:
            n=numsSet.pop()
            if n not in lengthMap:
                lengthMap[n]=1
            target=n+1
            while target in lengthMap or target in numsSet:
                if target in lengthMap:
                    lengthMap[n]+= lengthMap[target]
                    target+=lengthMap[target]
                elif target in numsSet:
                    lengthMap[n]+=1
                    numsSet.remove(target)
                    target += 1
            longest=max(longest,lengthMap[n])
        return longest