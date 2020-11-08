/***
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
 */


class Solution{
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    List<Integer> path =  new ArrayList<Integer>();

    public List<List<Integer>> subsets(int [] nums){
        dfs(nums, 0);
        return res;
    }

    // 明确每一层递归函数里面解决的是：
    // nums数组中每一个可选值，选/不选----> 
    // 所以递归结束的条件就清楚了，
    // 在没有其他的要求的情况下（77中有k的限制，可以提前终止），
    // 结束递归就是nums中所有的可选值都被考虑过，即cur==nums.length


    public void dfs(int [] nums, int cur){
        if(cur==nums.length){
            res.add(new ArrayList<Integer>(path));
            return;
        }
        path.add(nums[cur]);
        dfs(nums, cur + 1);
        path.remove(path.size() - 1);
        dfs(nums, cur + 1);
    }
}