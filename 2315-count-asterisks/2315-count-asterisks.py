class Solution:
    def countAsterisks(self, s: str) -> int:
        positions = [i for i, char in enumerate(s) if char == "|"]
        count=0
        for char in s:
            if char=="*":
                count+=1
        pairs = [[positions[i] for i in range(n*2, n*2+2)] for n in range(len(positions)//2)]
        exclude=0
        for pair in pairs:
            #for char in s[pair(0):pair(1)]:
            for char in s[pair[0]:pair[1]]:
                if char=="*":
                    exclude+=1
        return count-exclude



        