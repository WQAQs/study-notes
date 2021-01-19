import java.util.List;
import java.util.ArrayList;

public class pathSum_offer_34 {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();

    List<List<Integer>> pathSum(TreeNode root, int tar) {
        if(root == null) return res;
        recur(root, tar);
        return res;
    }
    void recur(TreeNode root, int tar){
        if(root == null) return;
        path.add(root.val);
        if(tar - root.val == 0 && root.left == null && root.right == null){
            res.add(new ArrayList<Integer>(path));
        }
        recur(root.left, tar - root.val);
        recur(root.right, tar - root.val);
        path.remove(path.size() - 1); // 向上回溯前，将当前节点从path中删除
    }


    public static void main(String[] args){
        serialize_and_deserialize_297 testcode = new serialize_and_deserialize_297();
        pathSum_offer_34 mytest = new pathSum_offer_34();
        TreeNode root;
        String temp = "5,4,11,None,None,None,8,13,None,None,4,None,None";
        root = testcode.deserialize(temp);
        String s = testcode.serialize(root);
        System.out.println(s);
        List<List<Integer>> res = mytest.pathSum(root, 1);
        System.out.println(res);
    }
}
