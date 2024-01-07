class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j]<nums[i] and j!=i:
                     count +=1
            ans.append(count)
        return ans
        