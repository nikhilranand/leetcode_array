class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def negative(arr,x):
            low,high=0,len(arr)-1
            ans=len(arr)
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>x:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def positive(arr,x):
            low,high=0,len(arr)-1
            ans=len(arr)
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>x:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return len(arr)-ans
        neg=negative(nums,-1) 
        pos=positive(nums,0)
        return max(pos,neg)

        
        