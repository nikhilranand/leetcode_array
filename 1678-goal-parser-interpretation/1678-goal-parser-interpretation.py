class Solution:
    def interpret(self, command: str) -> str:
      
        result = ""
        index = 0
        while index < len(command):
            if command[index:index+4] == "(al)":
                result += "al"
                index += 4
            elif command[index:index+2] == "()":
                result += "o"
                index += 2
            else:
                result += command[index]
                index += 1
        return result





