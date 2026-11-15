class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int difference = 0;
        int end = numbers.size() -1;
        int begin  = 0;
        for(int i = 0; i < numbers.size(); i++){
           if (numbers[end] + numbers[begin] == target){
            return {begin + 1, end + 1};
           } else if(numbers[end] + numbers[begin] < target){
            begin = begin + 1;
           }
           else {
            end = end -1;
           }
        }


        return {};
    }
};
