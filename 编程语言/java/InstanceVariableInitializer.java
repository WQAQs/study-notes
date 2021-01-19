public class InstanceVariableInitializer {  

    private int i = 1;  //（1）
    private int j = i + 1;  //（2）

    public InstanceVariableInitializer(int var){ // (0)
        System.out.println(i);  // (4)
        System.out.println(j);  // (5)
        this.i = var;           // (6)
        System.out.println(i);  // (7)
        System.out.println(j);  // (8)
    }

    {               // 实例代码块
        j += 3; // (3)

    }

    public static void main(String[] args) {
        new InstanceVariableInitializer(8);
    }
}/* Output: 
            1
            5
            8
            5
 *///:~