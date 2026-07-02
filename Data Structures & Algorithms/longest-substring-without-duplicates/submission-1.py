class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        chars = set()
        maxLen = 0

        while j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                maxLen = max(j-i, maxLen)
            else:
                while s[j] in chars:
                    chars.remove(s[i])
                    i += 1

        return maxLen