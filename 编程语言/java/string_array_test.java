import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class string_array_test {
    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root);
        String[][] res = new String[height][(1 << height) - 1];
        int t1 = res[0].length;
        for(String[] arr:res)
            Arrays.fill(arr,"");
        int t2 = res[0].length;
        List<List<String>> ans = new ArrayList<>();
        // fill(res, root, 0, 0, res[0].length);
        for(String[] arr:res)
            ans.add(Arrays.asList(arr));
        return ans;
    }

    public void fill(String[][] res, TreeNode root, int i, int l, int r) {
        if (root == null)
            return;
        res[i][(l + r) / 2] = "" + root.val;
        fill(res, root.left, i + 1, l, (l + r) / 2);
        fill(res, root.right, i + 1, (l + r + 1) / 2, r);
    }
    public int getHeight(TreeNode root) {
        if (root == null)
            return 0;
            return 1 + Math.max(getHeight(root.left), getHeight(root.right));
        }

    public static void main(String[] args) {
        // serialize_and_deserialize_297 testcode = new serialize_and_deserialize_297();
        // TreeNode root;
        // String temp = "30,-1,None,21,None,None,40,33,None,None,46,None,None";
        // root = testcode.deserialize(temp);
        // String s = testcode.serialize(root);
        // System.out.println(s);

        // string_array_test mytest = new string_array_test();
        // List<List<String>> res = mytest.printTree(root);
        String s = "01234";
        String[][] t0 = {{"01234"}};
        List<String> t1 = new ArrayList<>();
        List<List<String>> t2 = new ArrayList<>();
        t1.add(s);
        t2.add(t1);
        List<String> t3 = t2[0]; 

     }
    
}
