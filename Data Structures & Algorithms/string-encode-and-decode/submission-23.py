class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            subLen = int(s[i:j])
            decoded.append(s[j+1:j+1 + subLen])
            i = j + subLen + 1

        return decoded