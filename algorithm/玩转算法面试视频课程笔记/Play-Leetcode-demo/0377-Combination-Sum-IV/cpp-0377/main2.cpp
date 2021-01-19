/// Source : https://leetcode.com/problems/combination-sum-iv/description/
/// Author : liuyubobobo
/// Time   : 2018-02-28
/// updated: 2019-03-31

#include <iostream>
#include <vector>

using namespace std;


/// Dynamic Programming
/// Time Complexity: O(n * target)
/// Space Complexity: O(target)
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {

        int n = nums.size();
        if(n == 0)
            return 0;

        vector<int> memo(target + 1, 0);
        memo[0] = 1;

        for(int i = 1; i <= target; i++)
            for(int j = 0; j < n; j ++)
                if(nums[j] <= i){
                    if(memo[i] == -1 || memo[i - nums[j]] == -1 ||
                       (long long)memo[i] + (long long)memo[i - nums[j]] > INT_MAX)
                        memo[i] = -1;
                    else memo[i] += memo[i - nums[j]];
                }
        assert(memo[target] != -1);
        return memo[target];
    }
};


int main() {

    vector<int> nums1 = {1, 2, 3};
    int target1 = 4;
    cout << Solution().combinationSum4(nums1, target1) << endl;

    return 0;
}