class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = dict()
        tFreq = dict()

        for c in s:
            if c not in sFreq:
                sFreq[c] = 1
            else:
                sFreq[c] += 1
               
        for c in t:
            if c not in tFreq:
                tFreq[c] = 1
            else:
                tFreq[c] += 1

        if len(sFreq) != len(tFreq):
            return False

        for x in sFreq:
            if x not in tFreq or sFreq[x] != tFreq[x]:
                return False

        return True