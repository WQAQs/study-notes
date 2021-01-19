/**
 * 77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
 */
class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>(); // 里层的尖括号里面必须要是List
                                                              // 不能是ArrayList
    List<Integer> path = new ArrayList<Integer>();

   public List<List<Integer>> combine(int n, int k){
        dfs(1, n, k);
        return res;
    }        
    public void dfs(int cur, int n, int k){
        //记录合法的答案 （这两个if语句的顺序很重要！）
        if(path.size() == k){
            res.add(new ArrayList<Integer>(path));  // 要重新new一个，
                                                    // 否则指向的可变的path对象
            return;
        }
        //没有可选，结束递归
        if(cur == n + 1)
            return;
        //选择当前数
        path.add(cur);
        dfs(cur + 1, n, k);
        //回溯，重置状态
        path.remove(path.size() - 1);
        //不选择当前数，进行递归
        dfs(cur + 1, n, k);
    }
}