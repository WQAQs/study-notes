import java.util.ArrayList;
import java.util.List;

class Solution{
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    List<Integer> path = new ArrayList<Integer>();
    public List<List<Integer>> subsetsWithDup(int [] nums){
        Array.sort(nums);
        dfs(nums, 0);
        return res;
    }
    public void dfs(int [] nums, int cur){
        
        // 记录合法结果
        if(cur = nums.length){
            res.add(new ArrayList<Integer>(path));
            return;
        }
        // 选nums[cur]
        path.add(nums[cur]);
        dfs(nums, cur + 1);
        // 不选nums[cur]
        path.remove(path.size() - 1);
        dfs(nums, cur + 1);
    }
}