'''75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
'''
## 1.计数排序
## 时间复杂度：O(n)
## 空间复杂度：O(n)
def sortColors1(nums):
    freq = [0 for i in range(3)]
    for x in nums:
        freq[x] += 1
    nums[0:freq[0]] = [0 for i in range(freq[0])]
    nums[freq[0]:freq[0]+freq[1]] = [1 for i in range(freq[1])]
    nums[freq[0]+freq[1]:freq[0]+freq[1]+freq[2]] = [2 for i in range(freq[2])]


#使用双索引
def sortColors2(nums):
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

nums = [2,0,2,1,1,0]
res = sortColors1(nums)
res