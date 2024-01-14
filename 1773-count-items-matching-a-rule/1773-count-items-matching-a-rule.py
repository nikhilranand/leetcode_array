class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n=len(items)
        count=0
        for item in items: 
            if ruleKey=='type' and ruleValue==item[0]:
                count+=1
            if ruleKey=='color' and ruleValue==item[1]:
                count+=1
            if ruleKey=='name' and ruleValue==item[2]:
                count+=1
        return count
       