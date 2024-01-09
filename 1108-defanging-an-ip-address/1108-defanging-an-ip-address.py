class Solution:
    def defangIPaddr(self, address: str) -> str:
        add=""
        for char in address:
            if "." == char:
                add=address.replace(".", "[.]")
        return add
        