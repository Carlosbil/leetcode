#include <map>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> miMapa;
        for(int i = 0; i < nums.size(); i++){
            int to_find = target - nums[i];
            if (miMapa.find(to_find) != miMapa.end()) {
                return {miMapa[to_find], i};
            };
            miMapa[nums[i]] = i;
        }
        return {};
    };
};