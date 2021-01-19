import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;

class grammar_test{
    int x = -5;
    int compute(int x, int w){
        return x / w;
    }
    public static void main(String[] args) {
        /* 建立一个Collection */
        String[] strings = {"A", "B", "C", "D"};
        Collection stringList = java.util.Arrays.asList(strings);
        /* 开始遍历 */
        for (Iterator itr = stringList.iterator(); itr.hasNext();) {
        Object str = itr.next();
        System.out.println(str);
 }

        grammar_test test = new grammar_test();
        int a = test.compute(-5, 5);
        int b = test.compute(-3, 5);
        int c = test.compute(-6, 5);
        int d = test.compute(3, 5);
        System.out.print(new ArrayList<>(Arrays.asList(a,b,c,d)));
    }
}