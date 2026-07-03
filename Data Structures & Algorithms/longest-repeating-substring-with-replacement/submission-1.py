from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
        freq = defaultdict(int)
        i = 0
        maxFreq = 0
        maxLen = 0
        


        for j in range(len(s)):
            freq[s[j]] += 1
            maxFreq = max(maxFreq, freq[s[j]])

            while (j - i + 1) - maxFreq > k:
                freq[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j - i + 1)
                

        return maxLen



