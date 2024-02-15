class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def lower_bound(arr,x):
           low,high=0,len(arr)-1
           ans=len(arr)
           while low<=high:
               mid=(low+high)//2
               if arr[mid]>=x:
                   ans=mid
                   high=mid-1
               else:
                   low=mid+1
           if ans==len(arr):
               return -1
           else:
               return ans
        #nums=set(arr)
        #arr1=list(nums)
        op=[]
        #first=lower_bound(nums,x)
        maximum=max(arr)
        for i in range(1,maximum+1):
            first=lower_bound(arr,i)
            if first==-1 or arr[first]!=i:
                op.append(i)
        while len(op)<k:
            op.append(maximum+1)
            maximum+=1
        return op[k-1]

        