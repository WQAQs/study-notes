import java.util.List;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Collection;

public class serialize_and_deserialize_297 {


    // public String rserialize(TreeNode root, String str) {
    //     if (root == null) {
    //         str += "None,";
    //     } else {
    //         str += String.valueOf(root.val) + ",";
    //         str = rserialize(root.left, str);
    //         str = rserialize(root.right, str);
    //     }
    //     return str;
    // }
  
    // public String serialize(TreeNode root) {
    //     return rserialize(root, "");
    // }
  
    // public TreeNode rdeserialize(List<String> l) {
    //     if (l.get(0).equals("None")) {
    //         l.remove(0);
    //         return null;
    //     }
  
    //     TreeNode root = new TreeNode(Integer.valueOf(l.get(0)));
    //     l.remove(0);
    //     root.left = rdeserialize(l);
    //     root.right = rdeserialize(l);
    
    //     return root;
    // }
  
    // public TreeNode deserialize(String data) {
    //     String[] data_array = data.split(",");
    //     List<String> data_list = new LinkedList<String>(Arrays.asList(data_array));
    //     return rdeserialize(data_list);
    // }

    // 使用【先序遍历】： 读取并存储二叉树结构（序列化）/ 构建二叉树（反序列化）
    public String serialize(TreeNode root) {
        return reserialize(root);
    }

    String reserialize(TreeNode root){
        if(root == null) return "None,";
        String left = reserialize(root.left);
        String right = reserialize(root.right);
        return String.valueOf(root.val) + "," + left + right;
    }
    
    public TreeNode deserialize(String data) {
        String[] temp = data.split(",");
        List<String> data_list = new LinkedList<String>(Arrays.asList(temp));
        return redeserialize(data_list);
    }
    TreeNode redeserialize(List<String> data_list){
        if(data_list.get(0).equals("None")){
            data_list.remove(0);
            return null;
        }
        TreeNode root = new TreeNode(Integer.valueOf(data_list.get(0)));
        data_list.remove(0);
        root.left = redeserialize(data_list);
        root.right = redeserialize(data_list);
        return root;
    }

    public static void main(String[] args){
        serialize_and_deserialize_297 testcode = new serialize_and_deserialize_297();
        TreeNode root;
        String temp = "1,2,None,None,3,4,None,None,5,None,None";
        root = testcode.deserialize(temp);
        String s = testcode.serialize(root);
        System.out.println(s);
    }
}

