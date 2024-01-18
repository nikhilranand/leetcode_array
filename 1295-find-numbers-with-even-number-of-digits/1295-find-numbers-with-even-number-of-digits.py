class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        #for num in nums:
        #    count=0
        #    while num>0:
        #        digit1=num%10
        #        count+=1
        #        digit2=num//10
        #    if count%2==0:
        #        ans+=1
        #return ans
        #time limit exceed in this code
        for num in nums:
            digits=int(math.log10(num))+1
            if digits%2==0:
                ans+=1
        return ans