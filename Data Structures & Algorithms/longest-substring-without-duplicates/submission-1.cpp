class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) return 0;
        unordered_map<char, int> freq;

        int maxLen = 0;

        int l = 0;
        int r = 0;
        while (r < s.length()) {
            if (freq[s[r]] == 0) {
                freq[s[r]]++;
                r++;

            } else {
                maxLen = max(r - l, maxLen);
                freq[s[l]]--;
                l++;
            }
        }

        return max(r - l, maxLen);
    }
};

