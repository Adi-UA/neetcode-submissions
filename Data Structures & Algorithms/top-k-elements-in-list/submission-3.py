class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq map {n:freq}
        # sort freq map by lambda which is the frequency
        freq_map=defaultdict(int)
        for n in nums:
            freq_map[n]+=1
        return sorted(freq_map,key=lambda x:freq_map[x],reverse=True)[:k]
            