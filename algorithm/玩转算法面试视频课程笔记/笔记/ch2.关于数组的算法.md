# **关于数组的算法**

## **1. 如何写出正确的程序**

**技巧**：

   > 1. 明确变量的含义，在写代码时要注意维护该含义（即维持循环不变量，变量的值会发生改变，但变量的含义不能改变）（观察，思考）
   >2. 考虑各种边界情况/特殊情况，比如待查找的数据集是空集，待查找的值不在数据集中，...
   >3. 小数据量调试(耐心)
   >4. 大数据量测试


**举例：二分查找法**

- **注意**：整型溢出
  
        mid = (l + r)/2

    因为l和r都是int型，当它们很大时，在做加法运算可能会出现整型溢出，C++中整型溢出是不报错的。

**实战:**

**1. leetcode 283 移动零**
**题目描述**：给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
   示例:
   输入: [0,1,0,3,12]
   输出: [1,3,12,0,0]
   说明:
   必须在原数组上操作，不能拷贝额外的数组。
   尽量减少操作次数。
**(1). 直接的想法**
   **思想**：扫描一遍数组，把非0元素拿出来，放在原数组前半部，原数组剩下的后半部直接置0。
   ```python
   def move_zeros(nums):
      nonzero_nums = []
      n = len(nums)
      for i in range(n):
            if nums[i]:
               nonzero_nums.append(nums[i])
      m = len(nonzero_nums)
      for i in range(m):
            nums[i] = nonzero_nums[i]
      for i in range(m, n):
            nums[i] = 0
      return nums
   ```
   时间复杂度：$O(n)$
   空间复杂度：$O(n)$
**(2). 优化**
   **思想**：不需要使用额外的数组保存非0元素，原数组nums[0,k)区间保存所有当前遍历过的非0元素；
    1. 初始时 k = 0，扫描原数组(i 标志扫描)，遇到非0元素就放在原数组k位置上，k ++ ，使得原数组[0,k)区间保存非0元素；
    2. 扫描完 (i == len(nums)), 将nums[k,len(n-1))范围内的数置0；

   ```python
   def move_zero(nums):
      k = 0
      for x in nums:
         if x:
            nums[k] = x
            k += 1
      while k < len(nums):
         nums[k] = 0
         k += 1
      return nums
   ```
   时间复杂度：$O(n)$
   空间复杂度：$O(1)$
**(3). 再优化**
   **思想**：不需要方法2中的步骤2，在扫描到非0元素时，将非0元素和0元素交换；
   ```python
   def move_zero(nums):
      k = 0
      for i in range(len(nums)):
         if nums[i]:
               nums[k], nums[i] = nums[i], nums[k]
               k += 1
      return nums
   ```

**2. leetcode 27 移除元素**
**题目描述**：给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
**思想**：nums[0,k)中存放不等于val的元素。具体实现是，扫描数组，当扫描到的数nums[i]!=val,就交换nums[k]和nums[i]
```python
## 使用滑动窗口nums[0,k)保存不等于val的项
def removeElement(self, nums: List[int], val: int) -> int:
   k = 0
   for i in range(len(nums)):
      if nums[i] != val:
         nums[k], nums[i] = nums[i], nums[k]
         k += 1
   return k
```
**3. leectode 26 删除排序数组中重复的元素**
**题目描述**：给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。
```python
## 使用滑动窗口nums[0,k]保存没有重复的项
def removeDuplicates(self, nums: List[int]) -> int:
   k = 0
   for i in range(1, len(nums)):
      if nums[i] != nums[k]:
         nums[k + 1] = nums[i]
         k += 1
   return k
```

**4. leetcode 80 删除数组中重复的元素II**
**题目描述**：给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。
```python
## 使用滑动窗口nums[0,k]保存满足题意的项
def removeDuplicates(self, nums: List[int]) -> int:
   if not len(nums):
      return 0
   dict_sub = {}  # 统计nums[0,k]中每个字符出现的次数
   k = 0
   dict_sub[nums[k]] = dict_sub.get(nums[k],0) + 1
   for i in range(1, len(nums)):
      if not (nums[k] == nums[i] and dict_sub.get(nums[i],0) >= 2):
            nums[k + 1] = nums[i]
            dict_sub[nums[k + 1]] = dict_sub.get(nums[k + 1],0) + 1
            k += 1
   return k + 1
```

## **3. 基础算法思路的应用**

### **3.1 leetcode 75 sort colors**

  >给定一个有n个元素的数组，数组中元素的取值只有0，1，2三种可能，为这个数组排序

  (1) **暴力方法**

   时间复杂度：$O(n^2)$

  (2) **计数排序**

   >**思路**：分别统计0，1，2的元素个数，然后依次将多少个0，多少个1，多少个2放回数组

   代码：

   ```python
   ## 时间复杂度：O(n)
   ## 空间复杂度：O(1)
   ## 遍历了整个数组2遍
   def sortColors1(nums):
    freq = [0 for i in range(3)]
    for x in nums:
        freq[x] += 1
    nums[0:freq[0]] = [0 for i in range(freq[0])]
    nums[freq[0]:freq[0]+freq[1]] = [1 for i in range(freq[1])]
    nums[freq[0]+freq[1]:freq[0]+freq[1]+freq[2]] = [2 for i in range(freq[2])]

   ```


  (3) **三路排序**

   >**思路**：设置索引`zero`，`two`，希望`nums[0,...zero] == 0, nums[zero+1, i-1]== 1, nums[two, n-1] == 2`, 初始值设置`zero = -1`，`two = n` （n是数组的大小）

   代码：

   ```python
   ## 时间复杂度：O(n)
   ## 空间复杂度：O(1)
   ## 遍历了整个数组1遍
   def sortColors(nums):
    zero = -1 #nums[0,zero]范围存放0颜色,nums[zero+1,i-1]范围存放1颜色
    two = len(nums) #nums[two,n-1]范围存放2颜色
    i = 0
    while i < two:
        if nums[i] == 1:
            i += 1 
        elif nums[i] == 0:
            zero += 1
            nums[i],nums[zero] = nums[zero],nums[i]
            i += 1
        elif nums[i] == 2:
            two -= 1
            nums[i],nums[two] = nums[two],nums[i]
    return nums
   ```


### **3.2 练习题**

  - leetcode 88 merge sorted array
  
    ```python
      ## 方法1：双指针/从前向后
      ##        申请一个空间为（m+n）的数组new_nums保存比较结果，然后再赋值给nums1
      ##        使用了3个索引，分别指向new_nums,nums1,nums2当前位置。
      ## 时间复杂度：O(m+n)
      ## 空间复杂度：O(m+n)
      def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
         """
         Do not return anything, modify nums1 in-place instead.
         """
         new_nums = [0 for i in range(m+n)]
         p1 = 0
         p2 = 0
         for i in range(m+n):
            if p1 < m and p2 < n:
                  if nums1[p1] <= nums2[p2]:
                     new_nums[i] = nums1[p1]
                     p1 += 1
                  else:
                     new_nums[i] = nums2[p2]
                     p2 += 1
            elif p1 >= m:
                  new_nums[i] = nums2[p2]
                  p2 += 1
            elif p2 >= n:
                  new_nums[i] = nums1[p1]
                  p1 += 1
         for i in range(m+n):
            nums1[i] = new_nums[i]

      ## 方法2:使用双指针/从前往后
      ##       申请一个空间为m的数组保存nums1的前m个元素
      ## 时间复杂度：O(m+n)
      ## 空间复杂度：O(m)
      def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
         nums1_copy = nums1[:m]
         # 注意！！！：nums1 = [] 效果和nums1[:] = [] 不一样
         #  nums1 = [],是重新创建了一个局部变量，后面的操作就都是
         #             对这个新创建的nums1的了，而对原来的nums1没有影响
         #  nums1[:] = [],是对原来的nums1的切片赋值操作
         nums1[:] = []
         p1 = 0
         p2 = 0
         while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                  nums1.append(nums1_copy[p1])
                  p1 += 1
            else:
                  nums1.append(nums2[p2])
                  p2 += 1
         if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:]  # 如果nums1还有剩下
         if p2 < n:
            nums1[p1+p2:] = nums2[p2:] # 如果nums2还有剩下
         
      ## 方法3:使用双指针/从后往前
      ##       不需要额外的空间，利用nums1的后面没用到的空间
      ## 时间复杂度：O(m+n)
      ## 空间复杂度：O(1)
      def merge3(nums1, m, nums2, n):
         p = m + n - 1
         p1 = m - 1
         p2 = n - 1
         while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                  nums1[p] = nums1[p1]
                  p1 -= 1
            else:
                  nums1[p] = nums2[p2]
                  p2 -= 1
            p -= 1
         nums1[:p2 + 1] = nums2[:p2 + 1]  #若原来nums1的数据已经放好了，nums2的数据还有剩的
                                          #就全放进nums1中
                                          
      ## 方法4:合并后排序
      ##       排序直接使用内带的sorted()函数
      ## 时间复杂度：O((n+m)log(n+m)),即sorted函数的时间复杂度
      ## 空间复杂度：sorted函数的空间复杂度，网上说是O(m+n)
      def merge3(nums1, m, nums2, n):
         nums1[:] = sorted(nums1[:m]+nums2)
    ```

  - leetcode 215 kth lagest element in an arraray
  
    ```python
      ## 1.直接想法，先排序后返回对应索引
      ## 时间复杂度：O(nlogn)
      ## 空间复杂度：O(n)  即sorted函数的
      def findKthLargest1(nums: List[int], k: int) -> int:
         nums[:] = sorted(nums)
         return nums[len(nums)-k]

      ## 2.使用最小堆
      ## 时间复杂度:O(nlogk)
      ## 空间复杂度:O(k)
      def findKthLargest2(nums: List[int], k: int) -> int:
         return heapq.nlargest(k,nums)[-1]

      ## 3.快速选择
      ## 时间复杂度：平均情况下O(nlogn),最坏情况下O(n^2)
      ## 空间复杂度：O(1)
      def findKthLargest3(nums: List[int], k: int) -> int:
         def select(nums,start,end,k):
            if start > end:
                  return
            pivot_index = division(nums,start,end)
            if pivot_index == k:
                  return nums[pivot_index]
            elif pivot_index > k:
                  return select(nums,start,pivot_index-1,k)
            elif pivot_index < k:
                  return select(num s,pivot_index+1,end,k)
         def division(nums,start,end):
            pivot = nums[start]
            left = start
            right = end
            while left < right:
                  while left < right and pivot <= nums[right]:
                     right -= 1
                  nums[left] = nums[right]
                  while left < right and pivot > nums[left]:
                     left += 1
                  nums[right] = nums[left]
            nums[left] = pivot
            return left
         return select(nums,0,len(nums)-1,len(nums)-k)
    ```

- leetcode 167 two sum II — input array is sorted
   1. 暴力解法

        ```python
      ## 1.使用暴力法，双层遍历  ！！！超时！！！
      ## 时间复杂度：O(n^2)
      ## 空间复杂度：O(1)
      def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                  if nums[i] + nums[j] == target:
                     return [i+1,j+1]
         return 0 
        ```


   2. 二分搜索

      >**思路**： 充分利用原数组的性质——有序。依次遍历每一个数据`nums[i]`, 对于每一个`nums[i]`在剩余的数组中使用二分查找的思路来寻找`target - nums[i]`, 如果找到了的话，就找到了两个数相加结果为`target`,否则继续往后遍历。

      代码：

      ```python
      ## 2.使用二分搜索
      ## 时间复杂度：O(nlogn)
      ## 空间复杂度：O(1)
      def twoSum(self, nums: List[int], target: int) -> List[int]:
         def binary_search(nums,l,r,value):
            while l <= r:
                  mid = l + (r - l)//2  ## 注意整除要用// ，用/会得到floa型！！！
                  if nums[mid] == value:
                     return mid
                  elif nums[mid] < value:
                     l = mid + 1
                  elif nums[mid] > value:
                     r = mid - 1
            return -1
         for i in range(len(nums)):
            j = binary_search(nums,i+1,len(nums)-1,target-nums[i])
            if j != -1:
                  return [i+1,j+1]
      ```

# 3-7

## 双索引（双指针）技术

  定义好两个索引的含义，使用一定的规则去移动它们。

  1. **对撞指针**

     >前面的例子中两个指针向相对的方向行进，在这个过程中就可能找到我们要求解的答案。

  2. **滑动窗口**

     >两个索引构成一个窗口，让这个窗口不停地滑动，来在数组中找到要求解的答案。
  
- **例题** leetcode 209 minimum size subarray sum

   (1) **暴力解**

   **思路**：遍历所有的连续子数组$[i,...,j]$,
      计算其和`sum`,验证`sum >= s`,时间复杂度为$O(n^3)$

   (2) **优化暴力解**

   **思路**：优化暴力解中的求和`sum`的过程，时间复杂度$O(n^2)$

   (3) **滑动窗口**
  ```python
   def min_sub_array_len(s, nums):
   l = 0
   r = -1 # nums[l,...,r]为滑动窗口
   sum = 0 # 初始时候，nums[0,-1]范围内没有数，sum=0
   n = len(nums)
   res = n + 1
   while l < n:
      if r + 1 < n and sum < s:
         r += 1
         sum += nums[r]
      else:
         sum -= nums[l]
         l += 1
      if sum >= s:
         res = min(res, r - l + 1)
   if res == n + 1:
      return 0
   else:
      return res
  ```
# 3-8

- **leetcode 3 longest substring without repeating characters**
  **题目描述**: 
   > 3 . 无重复字符的最长子串
   给定一个字符串,请你找出其中不含有重复字符的最长子串的长度。
   示例:
   输入: "abcabcbb"
   输出: 3 
   解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
  
  **思路分析**：使用滑动窗口遍历子串；使用freq数组记录子串中字符出现次数，判断是否有重复字符时只用查询freq[i]是否为1，为1表示子串中已经有该字符。（i是查询字符的ASII码）

  **代码**：
  ```python
   ## 使用滑动窗口
   ## 注意python中字符转换为ASCII码要使用ord(),
   ## 不能用int(),int()只能将数字字符转换为对应的整数
   def lengthOfLongestSubstring(s):
      l = 0
      r = -1 # s[l,r]范围内保存不重复子串
      freq = [0 for i in range(256)] # 保存字符在子串中出现的次数，索引为字符的scii值
      res = 0
      while l < len(s):
         if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
               r += 1
               freq[ord(s[r])] += 1
         else:
               freq[ord(s[l])] -= 1
               l += 1
         res = max(res, r - l + 1)
      return res
  ```

- **练习题**
 leetcode 438.找到字符串中所有字母异位词
  ```python
   '''
   438. 找到字符串中所有字母异位词
   给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，
   返回这些子串的起始索引。

   字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

   说明：
   字母异位词指字母相同，但排列不同的字符串。
   不考虑答案输出的顺序。

   示例:

   输入:
   s: "abab" p: "ab"

   输出:
   [0, 1, 2]

   解释:
   起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
   起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
   起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

   '''
   ## 使用滑动窗口[l,r]
   def findAnagrams(s: str, p: str) -> List[int]:
      def check_same(freq_s,freq_p):
            for i in range(26):
               if freq_p != freq_s:
                  return False
            return True
      res = []
      l = 0
      r = -1
      freq_s=[0 for i in range(26)]
      freq_p=[0 for i in range(26)]
      for i in range(len(p)):
            freq_p[ord(p[i])-ord('a')] += 1
      while r + 1 < len(s) and len(p) > 0:
            r += 1
            freq_s[ord(s[r]) - ord('a')] += 1
            if r - l + 1 > len(p):
               freq_s[ord(s[l])-ord('a')] -= 1
               l += 1
            if r - l + 1 == len(p) and check_same(freq_s,freq_p):
               res.append(l)
      return res
  ```
  leetcode 76.最小覆盖子串
  
   ```python
   '''76. 最小覆盖子串
   给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

   示例：

   输入: S = "ADOBECODEBANC", T = "ABC"
   输出: "BANC"
   说明：

   如果 S 中不存这样的子串，则返回空字符串 ""。
   如果 S 中存在这样的子串，我们保证它是唯一的答案。
   '''
   def minWindow(self, s: str, t: str) -> str:
      def check_in(freq_s,freq_t):
            for i in range(256):
               if freq_t[i] != 0 and freq_t[i] > freq_s[i]:
                  return False
            return True
      l = 0
      r = -1
      freq_s = [0 for i in range(256)]
      freq_t = [0 for i in range(256)]
      res_len = len(s) + 1
      res_l = -1
      for char in t:
            freq_t[ord(char)] += 1
      while l < len(s):
            if r + 1 < len(s) and not check_in(freq_s,freq_t): # 没找到并且没找到底，继续往后找(r += 1)
               r += 1
               freq_s[ord(s[r])] += 1
            else:  # 找到底了，或者找到满足的子串了
               freq_s[ord(s[l])] -= 1      
               l += 1
            if r - l + 1 >= len(t) and check_in(freq_s,freq_t):  # 找到了一个满足题意的子串
               if r - l + 1 < res_len:  # 更新res_len
                  res_l = l
                  res_len = r - l + 1
      if res_len == len(s) + 1:
            return ""
      return s[res_l:res_l+res_len]
   ```
