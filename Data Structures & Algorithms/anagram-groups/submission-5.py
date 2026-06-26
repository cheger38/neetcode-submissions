import string

def getKey(s):
    freq = dict()

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    key = ""
    for char in string.ascii_lowercase:
        if char in freq:
            key += char * freq[char]
    
    return key


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = dict()

        for i, s in enumerate(strs):
            key = getKey(s)
            if key in mapping:
                mapping[key].append(i)
            else:
                mapping[key] = [i]
        
        groups = []
        for key in mapping:
            subset = []
            for i in mapping[key]:
                subset.append(strs[i])
            groups.append(subset)

        return groups



