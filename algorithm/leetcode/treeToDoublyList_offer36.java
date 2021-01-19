
public class treeToDoublyList_offer36 {
    
    // // Definition for a TreeNode.
    // class TreeNode {
    //     public int val;
    //     public TreeNode left;
    //     public TreeNode right;

    //     public TreeNode() {}

    //     public TreeNode(int _val) {
    //         val = _val;
    //     }

    //     public TreeNode(int _val,TreeNode _left,TreeNode _right) {
    //         val = _val;
    //         left = _left;
    //         right = _right;
    //     }
    // };

    // TreeNode min;  // 以root为根的树中最小的节点
    // TreeNode max; // 以root为根的树中最大的节点

    public  TreeNode treeToDoublyList(TreeNode root) {
        if(root == null) return null;
        TreeNode p = root;
        while(p.left != null) p = p.left;
        TreeNode head = p;
        p = root;
        while(p.right != null) p = p.right;
        TreeNode tail = p;
        build_linkedlist(root);
        head.left = tail;
        tail.right = head;
        return head;
    }

    void  build_linkedlist(TreeNode root){
        TreeNode pre = recur(root.left, true);
        TreeNode next = recur(root.right, false);
        if(pre != null){
            pre.right = root;
            root.left = pre;
        }
        if(next != null){
            next.left = root;
            root.right = next;
        }
    }


    TreeNode recur(TreeNode root, boolean isleft){
        if(root == null) return root;
        if(root.left == null && root.right == null) return root;
        TreeNode min = getMin(root);
        TreeNode max = getMax(root);
        
        TreeNode pre = recur(root.left, true);
        TreeNode next = recur(root.right, false);

        if(pre != null){
            pre.right = root;
            root.left = pre;
        }
        if(next != null){
            next.left = root;
            root.right = next;
        }
        // if(isleft) return next == null ? root : next;
        // else return pre == null ? root : pre; // 属于上一层的右子树，应该返回大中最小的
        if(isleft) return max; // 属于上一层的左子树，应该返回小中最大的
        else return min; // 属于上一层的右子树，应该返回大中最小的
    }

    TreeNode getMin(TreeNode root){
        TreeNode p = root;
        while(p.left != null) p = p.left;
        return p;
    }

    TreeNode getMax(TreeNode root){
        TreeNode p = root;
        while(p.right != null) p = p.right;
        return p;
    }

    public static void main(String[] args){
        serialize_and_deserialize_297 testcode = new serialize_and_deserialize_297();
        treeToDoublyList_offer36 mytest = new treeToDoublyList_offer36();
        TreeNode root;
        String temp = "27,-99,None,-34,None,-8,None,8,None,None,55,None,58,None,59,None,68,None,None";
        root = testcode.deserialize(temp);
        String s = testcode.serialize(root);
        System.out.println(s);
        TreeNode head = mytest.treeToDoublyList(root);
        System.out.println(head.val);
    }
}

