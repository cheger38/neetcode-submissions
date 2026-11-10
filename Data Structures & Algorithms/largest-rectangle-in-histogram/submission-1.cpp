class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<int> leftExtend(heights.size());
        vector<int> rightExtend(heights.size());

        // Calculate right extensions
        stack<pair<int, int>> st;
        for (int i = 0; i < heights.size(); i++) {
            while (!st.empty() && heights[i] < st.top().first) {
                auto bar = st.top();
                st.pop();

                rightExtend[bar.second] = i - bar.second - 1;
            }

            st.push(pair{heights[i], i});
        }

        while (!st.empty()) {
            auto bar = st.top();
            st.pop();

            rightExtend[bar.second] = heights.size() - bar.second - 1;
        }

        // Calculate left extensions
        for (int i = heights.size() - 1; i >= 0; i--) {
            while (!st.empty() && heights[i] < st.top().first) {
                auto bar = st.top();
                st.pop();

                leftExtend[bar.second] = bar.second - i - 1;
            }

            st.push(pair{heights[i], i});
        }

        while (!st.empty()) {
            auto bar = st.top();
            st.pop();

            leftExtend[bar.second] = bar.second;
        }


        // Find max rectangle
        int maxRect = -1;
        for (int i = 0; i < heights.size(); i++) {
            int rect = (1 + leftExtend[i] + rightExtend[i]) * heights[i];

            maxRect = max(rect, maxRect);
        }

       return maxRect;
    }
};
