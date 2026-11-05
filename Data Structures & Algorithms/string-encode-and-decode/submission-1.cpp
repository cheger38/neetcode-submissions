class Solution {
public:

    string encode(vector<string>& strs) {
        string res{};

        for (const string& s : strs) {
            res += std::to_string(s.length()) + "#" + s;
        }

        return res;
    }

    vector<string> decode(string s) {
        int l = 0;
        int r = 0; 

        vector<string> res{};
        while (r < s.length()) {
            if (s[r] != '#') {
                r++;
                continue;
            }

            int sLen = std::stol(s.substr(l, r - l));
            res.push_back(s.substr(r + 1, sLen));
            l = r + 1 + sLen;
            r = l;
        }

        return res;
    }
};
