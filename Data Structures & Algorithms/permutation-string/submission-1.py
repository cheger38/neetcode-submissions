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
            permFound = True
            for i in range(l, r + 1):
                c = s2[i]
                if s1counts[c] != s2counts[c]:
                    permFound = False
                    break

            if permFound: return True

            s2counts[s2[l]] -= 1
            l += 1

            r += 1
            if r == len(s2): break
            s2counts[s2[r]] += 1

        
        return False