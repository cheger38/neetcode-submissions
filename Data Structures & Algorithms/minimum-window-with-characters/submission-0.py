from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounts = defaultdict(int)
        for c in t:
            tCounts[c] += 1
        
        minSubStr = ""
        sCounts = defaultdict(int)
        l, r = 0, 0
        matches = 0
        while r < len(s):
            rc = s[r]
            if rc in tCounts:
                sCounts[rc] += 1
                if sCounts[rc] == tCounts[rc]:
                    matches += 1
            r += 1

            while matches == len(tCounts):
                if minSubStr == "" or r - l < len(minSubStr):
                    minSubStr = s[l:r]

                lc = s[l]
                if lc in tCounts:
                    if sCounts[lc] == tCounts[lc]:
                        matches -= 1
                    sCounts[lc] -= 1


                l += 1

        return minSubStr

        

