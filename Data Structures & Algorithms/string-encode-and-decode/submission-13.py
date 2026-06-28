class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "👋"

        encoded = ""
        for s in strs[:-1]:
            encoded += s
            encoded += "☕"

        encoded += strs[-1]
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        if s == "👋":
            return []
            
        decoded = []

        last_sep = -1
        i = 0
        while i < len(s):
            if s[i] == "☕":
                decoded.append(s[last_sep+1:i])
                last_sep = i

            i += 1
        
        decoded.append(s[last_sep+1:i])
        print(decoded)

        return decoded
            
           

