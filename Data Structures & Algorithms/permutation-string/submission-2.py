from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1counts = defaultdict(int)
        for c in s1:
            s1counts[c] += 1
        
        l, r = 0, 0

        s2counts = defaultdict(int)
        for i in range(len(s1)):
            s2counts[s2[i]] += 1
            r = i

        while r < len(s2):
            if s1counts == s2counts: return True

            s2counts[s2[l]] -= 1
            if s2counts[s2[l]] == 0: del s2counts[s2[l]]
            l += 1

            r += 1
            if r == len(s2): break
            s2counts[s2[r]] += 1

        
        return False