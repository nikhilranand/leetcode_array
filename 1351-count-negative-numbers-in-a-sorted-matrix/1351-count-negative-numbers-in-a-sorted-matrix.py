class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #count=0 
        #
        #for i in range(len(grid)):
        #    a,b=0,len(grid)
        #    
        #    while a<b:
        #        mid=a+(b-a)//2
        #        if grid[i][mid]<0:
        #             b=mid
        #        else:
        #            a=mid+1
        #    count+=len(grid[0])-a
        #return count
        #def bin(row):
        #    start, end = 0, len(row)
        #    while start<end:
        #        mid = start +(end -start) // 2
        #        if row[mid]<0:
        #            end = mid
        #        else:
        #            start = mid+1
        #    return len(row)- start
        #
        #count = 0
        #for row in grid:
        #    count += bin(row)
        #return(count)
        n=len(grid)
        m=len(grid[0])
        count=0
        for arr in grid:
            arr.sort()
            low,high=0,len(arr)-1
            ans = m

            while low <= high:
                mid = (low + high) // 2
                # maybe an answer
                if arr[mid] > -1:
                    ans = mid
                    # look for smaller index on the left
                    high = mid - 1
                else:
                    low = mid + 1  # look on the right
            count+=ans
        return count



        