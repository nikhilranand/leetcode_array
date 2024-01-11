class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(0,n,2):
            temp=[]
            freq=nums[i]
            val=nums[i+1]
            temp=[val]*freq
            #temp=val*freq
            #ans.append(temp)
            ans.extend(temp) #learn how to use extend
        return ans
        