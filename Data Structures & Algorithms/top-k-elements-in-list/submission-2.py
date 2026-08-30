class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for n in nums:
            freq_map[n]=freq_map.get(n,0)+1
        # sort by val
        sorted_lst=sorted(freq_map.items(),key=lambda item: item[1],reverse=True)
        return [k for k,v in sorted_lst[:k]]