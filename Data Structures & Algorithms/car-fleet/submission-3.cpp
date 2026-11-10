class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {

        vector<pair<int, int>> cars;

        for (int i = 0; i < position.size(); i++) {
            cars.push_back(pair{-position[i], i});
        }
        sort(cars.begin(), cars.end());

        stack<float> times;
        
        for (auto car : cars) {
            float carTime = (float)(target - (-car.first)) / speed[car.second];

            if (times.empty() || carTime > times.top()) {
                times.push(carTime);
            }
        }


        return times.size();
    }
};
