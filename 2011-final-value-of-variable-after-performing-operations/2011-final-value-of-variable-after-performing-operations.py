class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n=len(operations)
        X=0
        for i in range(n):
            if operations[i]=="X++":
                X+=1
            elif operations[i]=="++X":
                X+=1
            elif operations[i]=="X--":
                X-=1
            elif operations[i]=="--X":
                X-=1
        return X
            
        