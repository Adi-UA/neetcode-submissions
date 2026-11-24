class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=defaultdict(int)
        for n in nums:
            freq_map[n]+=1
        # now the freq's constrained by length of nums list
        sorted_nums=[[] for i in range(len(nums)+1)]
        for n,count in freq_map.items():
            sorted_nums[count].append(n)
        res=[]
        for lst in sorted_nums[::-1]:
            for n in lst:
                res.append(n)
                if len(res)==k:
                    return res