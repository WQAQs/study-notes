'''
80. 删除排序数组中的重复项 II
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。
'''
from typing import List
from collections import Counter
class Solution:
    ## 使用滑动窗口nums[0,k]保存满足题意的项
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        dict_sub = {}  # 统计nums[0,k]中每个字符出现的次数
        k = 0
        dict_sub[nums[k]] = dict_sub.get(nums[k],0) + 1
        for i in range(1, len(nums)):
            if not (nums[k] == nums[i] and dict_sub.get(nums[i],0) >= 2):## 注意dict.get(key,0)函数在dict中要是找不到键为key的项，
                                                                         ## 就返回0.如果参数中不写0，默认找不到key时返回none
                nums[k + 1] = nums[i]
                dict_sub[nums[k + 1]] = dict_sub.get(nums[k + 1],0) + 1
                k += 1
        return k + 1