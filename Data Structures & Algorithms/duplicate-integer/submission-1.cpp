
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> freq;

        for (int n : nums) {
            if (freq[n] == 1) {
                return true;
            }

            freq[n] += 1;
        }

        return false;
    }
};