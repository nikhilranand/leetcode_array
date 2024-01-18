class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sorted=sorted(seats)
        students_sorted=sorted(students) 
        n=len(seats)
        temp=0
        sum=0
        
        for i in range(n):
            temp= abs(seats_sorted[i]- students_sorted[i])
            sum+=temp
        return sum
