class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            a=nums[i]
            b=index[i]
            ans.insert(b,a)   #Understand the use of insert(index,value)
        return ans
        