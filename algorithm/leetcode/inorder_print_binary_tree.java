
public class inorder_print_binary_tree {
    void dfs(TreeNode root){
        if(root == null) return;
        dfs(root.left); // 左
        System.out.println(root.val); //根 （处理根节点）
        dfs(root.right); //右
    }
}
