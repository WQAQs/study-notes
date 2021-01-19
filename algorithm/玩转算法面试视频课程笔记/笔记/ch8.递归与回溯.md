递归与回溯
    树形问题
        17、letter combinations of a phone number
        --->递归调用的一个重要特征：要返回——回溯
            回溯法是暴力解法的主要实现手段：
                当要枚举所有的解时，在不能使用简单的循环来完成的话，就需要使用回溯法
        93、restore IP address
        131、拆分字符串，使得所有子串是回文字符串
    回溯算法的应用:
        排列问题：
            46、全排列数组（注意和问题17的不同，问题17中每一个数字代表固定的字符串，数字之间是独立的，而这里递归调用过程中，每取出一个数字都会影响递归调用要处理的数据范围，搜索的元素之间是互相冲突的，因此要注意将自己定义的一些状态进行回溯）
            47、全排列数组II（可能有相同元素）
        组合问题：
            77、组合
                优化：剪枝
            39、Combination Sum
            40、Combination Sum II
            216、Combination Sum III
            78、Subsets
            90、SubsetsII
            401、Binary Watch 
        二维平面上使用回溯法：
            79、Word Search
        二维平面上使用flooddill算法，一类经典问题：
        (注意并不同于回溯法，没有在返回的过程中堆一些状态重置)
            200、Number of  Islands
            130、Surrounded Regions
            417、Pacific Atlantic Water Flow
        回溯法是经典人工智能中：
            51、N-Queens
            52、N-Queens II
            37、Sudoku Solver
