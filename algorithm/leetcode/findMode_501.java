


public class findMode_501 {
    /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public int[] findMode(TreeNode root) {

    if(root == null) return new int[0];

    List<Integer> ans = new ArrayList<Integer>();
    List<Integer> res = new ArrayList<Integer>();

    inoder(root, ans); // 得到树的中序遍历结果（不递减的list）

    // 在list ans中搜索众数（注意ans中相同的数必然是连在一起的）
    res.add(ans.get(0)); // 初始化
    int curcount = 1, maxcount = 1;
    for(int i = 1; i < ans.size(); i++){ // 求递增list ans的众数
        // 计数（处理当前数），有(a)(b)两种可能：
        if(ans.get(i) == ans.get(i - 1)) 
            curcount++;// (a)
        else 
            curcount = 1; // (b)
        // 更新众数
        // 因为可能出现多个众数，他们出现的次数相同
        if(curcount == maxcount) 
            res.add(ans.get(i));
        else if(curcount > maxcount){
            res.clear();
            maxcount = curcount;
            res.add(ans.get(i));
        }
    }
    
    int[] temp = new int[res.size()];
    for(int i = 0; i < res.size(); i++){
        temp[i] = res.get(i);
    }
    return temp;
}
void inoder(TreeNode root, List<Integer> ans){
    if(root == null) return;
    inoder(root.left, ans);
    ans.add(root.val);
    inoder(root.right, ans);
}
}
