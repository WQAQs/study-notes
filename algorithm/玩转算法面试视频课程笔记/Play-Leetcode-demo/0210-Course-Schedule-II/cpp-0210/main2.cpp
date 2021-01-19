/// Source : https://leetcode.com/problems/course-schedule-ii/
/// Author : liuyubobobo
/// Time   : 2018-12-16

#include <iostream>
#include <vector>
#include <queue>

using namespace std;


/// Using Queue is enough
/// Since we are only interested in 0-indegree vertex :-)
///
/// Time Complexity: O(E)
/// Space Complexity: O(V + E)
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {

        vector<int> pre(numCourses, 0);
        vector<vector<int>> g(numCourses);
        for(const pair<int, int>& p: prerequisites){
            int from = p.second;
            int to = p.first;
            g[from].push_back(to);
            pre[to] ++;
        }

        queue<int> q;
        for(int i = 0; i < numCourses; i ++)
            if(pre[i] == 0)
                q.push(i);

        vector<int> res;
        while(!q.empty()){
            int id = q.front();
            q.pop();

            res.push_back(id);
            for(int next: g[id]){
                pre[next] --;
                if(pre[next] == 0)
                q.push(next);
            }
        }

        if(res.size() == numCourses)
            return res;
        return {};
    }
};


void print_vec(const vector<int>& vec){
    for(int e: vec)
        cout << e << " ";
    cout << endl;
}

int main() {

    vector<pair<int, int>> pre1 = {{1,0}};
    print_vec(Solution().findOrder(2, pre1));
    // 0 1

    vector<pair<int, int>> pre2 = {{1,0},{2,0},{3,1},{3,2}};
    print_vec(Solution().findOrder(4, pre2));
    // 0 1 2 3

    return 0;
}