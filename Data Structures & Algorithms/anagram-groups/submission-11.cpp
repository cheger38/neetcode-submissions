class Solution {
public:
    vector <vector<string>> groupAnagrams(vector<string>& strs) {
        auto ord = [](char c) {
            return c - 'a';
        };

        using char_frequency = std::array<int, 26>;
        std::map<char_frequency, std::vector<std::string>> groups;

        for (const string& s : strs) {
            char_frequency freq{};
            for (char c : s) {
                freq[ord(c)]++;
            }

            groups[freq].push_back(s);
        }

        vector<vector<string>> res;
        res.reserve(groups.size());

        for (const auto& pair : groups) {
            res.push_back(std::move(pair.second));
        }

        return res;
    }
};
