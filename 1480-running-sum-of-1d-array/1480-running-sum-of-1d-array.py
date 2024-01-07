class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        temp=0
        ans=[]
        for i in range(n):
            temp=temp+nums[i]
            ans.append(temp)
        return ans
