class Solution {
public:
    int characterReplacement(string s, int k) {
        // len <= maxf + k
        unordered_map<char, int> mp;
        int res = 0;

        int l = 0;
        int maxf = 0;
        for (int r = 0; r < s.length(); r++) {
            // Add next char to the window
            mp[s[r]]++;
            // Update maxf
            maxf = max(maxf, mp[s[r]]);

            // Shrink left until valid with current maxf (may invalidate)
            while ((r - l + 1) - maxf > k) {
                mp[s[l]]--;
                l++;
            }

            // Update res
            res = max(res, r - l + 1);
        }

        return res;
    }
};
