from io import StringIO

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:

        stream = StringIO(s)
        results = []

        while True:
            digits = ''

            while (char := stream.read(1)) and char.isdigit():
                digits += char

            if not digits:
                break
            
            string = stream.read(int(digits))
            results.append(string)

        return results




