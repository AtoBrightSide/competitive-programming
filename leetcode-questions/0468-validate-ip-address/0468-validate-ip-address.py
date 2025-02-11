class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        isHex = lambda s: s in "0123456789ABCDEFabcdef"
        if "." in queryIP and ":" in queryIP:
            return "Neither"
        
        if "." in queryIP and len(queryIP.split(".")) == 4:
            queryIP = queryIP.split(".")
            for part in queryIP:
                if (not part.isdigit()) or (not 0 <= int(part) <= 255):
                    return "Neither"
                leadingZero = part[0] == "0"
                if leadingZero and len(part) > 1:
                    return "Neither"
            return "IPv4"
        
        if ":" in queryIP and len(queryIP.split(":")) == 8:
            for part in queryIP.split(":"):
                if (not 1 <= len(part) <= 4) or (not all([isHex(ch) for ch in part])):
                    return "Neither"
                
            return "IPv6"
        return "Neither"