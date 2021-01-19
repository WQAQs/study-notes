/// Source : https://leetcode.com/problems/meeting-scheduler/
/// Author : liuyubobobo
/// Time   : 2019-10-19

#include <iostream>
#include <vector>

using namespace std;


/// Sorting and Two Pointers
/// Time Complexity: O(nlogn)
/// Space Complexity: O(1)
class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {

        sort(slots1.begin(), slots1.end(), [](const vector<int>& a, const vector<int>& b){
            if(a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });

        sort(slots2.begin(), slots2.end(), [](const vector<int>& a, const vector<int>& b){
            if(a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });

        int i = 0, j = 0;
        while(i < slots1.size() && j < slots2.size()){

            int a = max(slots1[i][0], slots2[j][0]);
            int b = min(slots1[i][1], slots2[j][1]);
            if(b > a && b - a >= duration) return {a, a + duration};

            if(slots1[i][0] < slots2[j][0]) i ++;
            else if(slots1[i][0] > slots2[j][0]) j ++;
            else if(slots1[i][1] < slots1[j][1]) i ++;
            else j ++;
        }
        return {};
    }
};


int main() {

    return 0;
}