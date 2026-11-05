class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> leftProd(nums.size(), 1);
        vector<int> rightProd(nums.size(), 1);

        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                leftProd[i] = nums[i];
            } else {
                leftProd[i] = nums[i] * leftProd[i-1];
            }
        }

        for (int i = nums.size() - 1; i > 0; i--) {
            if (i == nums.size() - 1) {
                rightProd[i] = nums[i];
            } else {
                rightProd[i] = nums[i] * rightProd[i+1];
            }
        }

        vector<int> res(nums.size());

        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                res[i] = rightProd[i+1];
            } else if (i == nums.size() - 1) {
                res[i] = leftProd[i-1];
            } else {
                res[i] = leftProd[i-1] * rightProd[i+1];
            }
        }

        return res;
    }
};
