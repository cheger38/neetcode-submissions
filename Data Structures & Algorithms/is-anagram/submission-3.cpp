class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        std::unordered_map<char, int> sFreq;
        std::unordered_map<char, int> tFreq;

        for (int i = 0; i < s.length(); i++) {
            sFreq[s[i]]++;
            tFreq[t[i]]++;
        }

        return sFreq == tFreq;
    }
};
