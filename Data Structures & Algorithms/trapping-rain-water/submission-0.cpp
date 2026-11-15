class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> maxLeft(height.size());
        vector<int> maxRight(height.size());

        for (int i = 0; i < height.size(); i++) {
            if (i == 0) {
                maxLeft[i] = height[i];
            } else {
                maxLeft[i] = max(maxLeft[i-1], height[i]);
            }
        }

        for (int i = height.size() - 1; i >= 0; i--) {
            if (i == height.size() - 1) {
                maxRight[i] = height[i];
            } else {
                maxRight[i] = max(height[i], maxRight[i+1]);
            }
        }

        int result = 0;
        for (int i = 0; i < height.size(); i++) {
            result += min(maxLeft[i], maxRight[i]) - height[i];
        }

        return result;
    }
};
