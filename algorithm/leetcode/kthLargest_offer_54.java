

public class kthLargest_offer_54{
    int c, res;
    public int kthLargest(TreeNode root, int k) {
        c = k;
        dfs(root);
        return res;
    }
    void dfs(TreeNode root){
        if(root == null) return;
        dfs(root.right);
        if(c == 0) return; 
        if(--c == 0) {
            res = root.val;
            return;
        }
        dfs(root.left);
    }


    public static void main(String[] args){
        serialize_and_deserialize_297 testcode = new serialize_and_deserialize_297();
        kthLargest_offer_54 mytest = new kthLargest_offer_54();
        TreeNode root;
        String temp = "30,-1,None,21,None,None,40,33,None,None,46,None,None";
        root = testcode.deserialize(temp);
        String s = testcode.serialize(root);
        System.out.println(s);
        int res = mytest.kthLargest(root, 1);
        System.out.println(res);
    }
}