class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        leftsum=[]
        rightsum=[]
        for i in range(n):
            temp=0
            #for j in range(, i):
            for j in range(0, i):
                temp=temp + nums[j]
            leftsum.append(temp)

        for i in range(n):
            temp1=0
            for j in range(i+1, n):
                temp1=temp1 + nums[j]
            rightsum.append(temp1)
        for i in range(n):
            temp2=0
            temp2=abs(leftsum[i]-rightsum[i])
            ans.append(temp2)
        return ans