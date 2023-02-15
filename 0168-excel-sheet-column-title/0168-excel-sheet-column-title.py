class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(64 + columnNumber + (26 if columnNumber == 0 else 0))
        curr = columnNumber % 26
        return self.convertToTitle((columnNumber // 26) - (0 if curr else 1) ) + self.convertToTitle(curr)