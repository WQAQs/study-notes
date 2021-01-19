public class TreeNode {
    // int val;
    // TreeNode left;
    // TreeNode right;
    // TreeNode(int x){val = x;}

    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode() {}

    public TreeNode(int _val) {
        val = _val;
    }

    public TreeNode(int _val,TreeNode _left,TreeNode _right) {
        val = _val;
        left = _left;
        right = _right;
    }
}

