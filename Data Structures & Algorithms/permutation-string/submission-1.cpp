class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        // s1 cannot be substring if s1 is longer than s2
        if (s1.length() > s2.length()) {
            return false;
        }

        unordered_map<char, int> freq1;
        for (char c : s1) {
            freq1[c]++;
        }
        

        for (auto item : freq1) {
            cout << item.first << ", " << item.second << '\n';
        }
        cout << "-------\n";


        unordered_map<char, int> freq2;
        for (int i = 0; i < s1.length(); i++) {
            freq2[s2[i]]++;
        }

        if (freq1 == freq2) {
            return true;
        }


        for (auto item : freq2) {
            cout << item.first << ", " << item.second << '\n';
        }
        cout << '\n';

        for (int i = 0; i < s2.length() - s1.length(); i++) {

            freq2[s2[i]]--;
            if (freq2[s2[i]] == 0) {
                freq2.erase(s2[i]);
            }
            freq2[s2[i + s1.length()]]++;

            if (freq1 == freq2) {
                return true;
            }
            
            for (auto item : freq2) {
                cout << item.first << ", " << item.second << '\n';
            }
            cout << '\n';

        }

        return false;
    }
};
