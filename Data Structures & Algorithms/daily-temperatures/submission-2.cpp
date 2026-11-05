class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size());

        stack<int> st;
        for (int i = 0; i < temperatures.size(); i++) {
            int curTemp = temperatures[i];

            while (!st.empty() && curTemp > temperatures[st.top()]) {
                int j = st.top();
                st.pop();

                res[j] = i - j;
            }

            st.push(i);
        }

        return res;
    }
};
