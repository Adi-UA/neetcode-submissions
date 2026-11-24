class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        zero_count=0
        for n in nums:
            if n==0:
                zero_count+=1
            else:
                total*=n
            if zero_count==2:
                return [0]*len(nums)
        res=[]
        for n in nums:
            if zero_count==1:
                if n!=0:
                    res.append(0)
                else:
                    res.append(total)
            else:
                res.append(int(total//n))
        return res