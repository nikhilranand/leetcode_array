class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        characters = [None] * len(s) 
        for i, index in enumerate(indices):
            characters[index] = s[i]  # Place characters at their correct indices
        
        return "".join(characters) 

        


