import java.util.Arrays;
import java.util.Queue;
import java.util.AbstractQueue;
import java.util.PriorityQueue;


public class array_copy_test {
    public static void main(String[] args)
     {
         int[] a = new int[10];
        
        //copyOf方法
        int[] copy = Arrays.copyOf(a, a.length * 2);
      //第一个参数为要拷贝的数组名，第二个为拷贝数组的大小(不限定大小，可用于扩大数组，如可以是a.length * 2)
 
       System.out.println(a[1] + " " +  copy[2] );
       AbstractQueue queue1;
     }

//     public static void main(String[] args) {
//         // 定义原数组，长度为8
//         int scores[] = new int[] { 100, 81, 68, 75, 91, 66, 75, 100 };

//         // 定义目标数组
//         // int newScores[] = new int[] { 80, 82, 71, 92, 68, 71, 87, 88, 81, 79, 90, 77 };
//         int[] newScores = (int[])Arrays.copyOf(scores,8);
//         System.out.println("原数组中的内容如下：");

//         // 遍历原数组
//         for (int i = 0; i < scores.length; i++) {
//             System.out.print(scores[i] + "\t");
//         }
//         System.out.println("\n目标数组中的内容如下：");

//         // 遍历目标数组
//         for (int j = 0; j < newScores.length; j++) {
//             System.out.print(newScores[j] + "\t");
//         }
//         // System.arraycopy(scores, 0, newScores, 0, 8);

//         // // 复制原数组中的一部分到目标数组中
//         // System.out.println("\n替换元素后的目标数组内容如下：");

//         // // 循环遍历替换后的数组
//         // for (int k = 0; k < newScores.length; k++) {
//         //     System.out.print(newScores[k] + "\t");
//         // }

//         scores[2] = -1;
//         scores[3] = -1;

//         System.out.println("\n\n修改后\n\n原数组中的内容如下：");

//         // 遍历原数组
//         for (int i = 0; i < scores.length; i++) {
//             System.out.print(scores[i] + "\t");
//         }
//         System.out.println("\n目标数组中的内容如下：");

//         // 遍历目标数组
//         for (int j = 0; j < newScores.length; j++) {
//             System.out.print(newScores[j] + "\t");
//         }
       
//     }
}
