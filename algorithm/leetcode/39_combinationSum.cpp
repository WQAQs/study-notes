#include <vector>

using namespace std;

/*
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> dp;
        vector<int> temp;
        int i = 1;
        return dp
    }
};

int main(){
    Solution so = new Solution();

}
*/

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ret;
        vector<int> now;
        int sum = 0, n = size(candidates);
        function<void(int)> dfs = [&] (int back) {
            if (sum == target) {
                ret.emplace_back(begin(now), end(now));
            } else if (sum > target) return;
            else {
                for (int i = back; i != n; ++i) {
                    now.push_back(candidates[i]);
                    sum += candidates[i];
                    dfs(i);
                    sum -= candidates[i];
                    now.pop_back();
                }
            }
        };
        dfs(0);
        return ret;
    }
};
