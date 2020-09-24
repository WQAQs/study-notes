#include <vector>

using namespace std;

class Solution
{
public:
    int coinChange(vector<int>& coins, int amount){
        vector<int> dp(amount + 1, INT16_MAX);
        dp[0] = 0;
        for(int i = 0; i < coins.size(); i++){
            for(int j = coins[i]; j < amount + 1; j++){
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};

int main(){
    Solution so = Solution();
    vector<int> coins = {1, 2, 5};
    int res = so.coinChange(coins, 11);
}


