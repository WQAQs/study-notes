# 数据规模的概念
- **如果想在1s之内解决问题**：

  O(n^2) 的算法可以处理大约10^4级别的数据

  O(n) : 10^8

  O(nlogn): 10^7

- **空间复杂度**

  一个辅助数组：O(n)

  一个辅助的二维数组：O(n)

  常数空间：O(n)

  递归调用是有空间代价的，递归调用的深度为n，则递归过程对应空间复杂度O(n)

- **时间复杂度分析**
  - 技巧

     一个和数据规模n正相关的循环：O（n）

     双重循环，每重循环都和数据规模正相关：O（n）
   
  - 实例复杂度分析
   <img style="width:400px;height:200px" src = "./images/O(n)1.png" alt="数字转换成字符串">

    <img style="width:400px;height:200px" src = "./images/O(n)2.png" alt="二分查找">

    <img style="width:400px;height:200px" src = "./images/O(nlogn).png">

    <img style="width:400px;height:200px" src = "./images/O(sqrt(n)).png" >

- 算法复杂度测试
 
  如测试A算法复杂度是否为O(n)? O(nlogn)? O(logn)?

  使数据规模n按照2倍递增，观察算法运行时间是否：
  
  1. 按照2倍递增： O(n)
  2. 按照2倍数多一点递增：O(nlogn)
     
     因为 $2nlog(2n)/nlogn = 2*（log2n/logn) =  2*（1 + log2/logn）\approx 2$

  3. 基本无变化：O(logn)

     因为 $log(2n)/nlogn = log2n/logn =  （log2 + logn)/logn = 1 + log2/logn$ 其中后一项很小，基本不影响时间复杂度
   
   例如：二分查找（复杂度为O(logn))的测试
       <img style="width:400px;height:200px" src = "./images/test1.png" >
- 递归算法的时间复杂度分析

   - 递归中进行一次递归调用的复杂度分析
     
     如果递归函数中，只进行一次递归调用，递归深度为depth；

     在每个递归函数中，使劲按复杂度为T；

     则总体的时间复杂度为O(T*depth)

