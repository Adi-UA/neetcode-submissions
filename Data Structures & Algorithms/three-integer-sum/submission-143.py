class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res=[]
        for i in range(len(nums)-2):
            # fixed is i
            l,r=i+1,len(nums)-1
            total=nums[i]+nums[l]+nums[r]
            while l < r:    
                if total == 0:
                    valid=[nums[l],nums[r],nums[i]]
                    if valid not in res:    
                        res.append(valid)
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    l+=1
                total=nums[i]+nums[l]+nums[r]
        return res