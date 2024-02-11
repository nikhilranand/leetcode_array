class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        #ans=[]
        #a,b=0,len(nums)-1
        #while a<b:
        #    
        #    mid=(a+b)//2
        #    if nums[mid]==target:
        #        if nums[mid-1]!=target and nums[mid+1]!=target and mid+1<=len(nums)-1 :
        #            ans.append(mid)
        #            break
        #        else:
        #            for i in range(a,b+1):
        #                if nums[i]==target:
        #                    ans.append(i)
        #            break
        #            
#
        #    elif nums[mid]<target:
        #        a=mid+1
        #    elif nums[mid]>target:
        #        b=mid-1
        #return ans
        #def index1(arr,x):
        #    a,b=0,len(arr)-1
        #    while a<b:
        #        mid=a+(b-a)//2
        #        if arr[mid]==x:
        #            return mid
        #            #if nums[mid-1]!=target and mid>0:
        #            #    return mid
        #            #else:
        #            #    a=mid-1
        #        elif arr[mid]<x:
        #            a=mid+1
        #        elif arr[mid]>x:
        #            b=mid
        #    return -1
        #def lastindex(arr,x):
        #    a,b=0,len(arr)
        #    while a<b:
        #        mid=a+(b-a)//2
        #        if arr[mid]==x:
        #            a=mid+1
        #           
        #        elif arr[mid]<x:
        #            a=mid+1
        #        elif arr[mid]>x:
        #            b=mid
        #    return b
        #nums.sort()
        #first_index = index1(nums, target)
        #last_index = lastindex(nums, target)
#
        #if first_index == -1:
        #    return []
#
        ## Generate indices in increasing order using slicing
        #return list(range(first_index, last_index + 1))
        #
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
        def upper_bound(arr,x):
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
        nums.sort()
        first_index=lower_bound(nums,target)
        last_index=upper_bound(nums,target)
        if first_index== -1:
            return []
        return list(range(first_index,last_index))
        

