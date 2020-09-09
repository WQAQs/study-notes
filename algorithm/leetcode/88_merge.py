from typing import List

## 方法1：申请一个空间为（m+n）的数组new_nums保存比较结果，然后再赋值给nums1
##        使用了三个索引，分别指向new_nums,nums1,nums2当前位置。
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

p2 = 1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
# nums1[:p2 + 1] = nums2[:p2 + 1]
res = merge2(nums1,3,nums2,3)
res