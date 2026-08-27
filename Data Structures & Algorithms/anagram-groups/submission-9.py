from collections import defaultdict
from string import ascii_lowercase

def getKey(s: str):
    freq = defaultdict(int)

    for c in s:
        freq[c] += 1 

    key = ""
    for c in ascii_lowercase:
        if c in freq:
            key += c * freq[c]
        
    return key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = dict()

        for s in strs:
            key = getKey(s)
            
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)

        return list(groups.values())
