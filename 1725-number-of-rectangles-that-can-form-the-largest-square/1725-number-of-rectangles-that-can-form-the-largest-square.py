class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        n=len(rectangles)
        ans=[]
        for rectangle in rectangles:
            minimum=min(rectangle)
            ans.append(minimum)
        maxi=max(ans)
        count=0
        for num in ans:
            if num==maxi:
                count+=1
        return count

        