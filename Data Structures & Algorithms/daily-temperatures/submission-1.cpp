class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size());

        stack<pair<int, int>> st;
        for (int i = 0; i < temperatures.size(); i++) {
            int curTemp = temperatures[i];

            while (!st.empty() && curTemp > st.top().first) {
                auto day = st.top();
                st.pop();

                res[day.second] = i - day.second;
            }

            st.push({curTemp, i});
        }

        return res;
    }
};
