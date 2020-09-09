from typing import List
import numpy as np



## 1. 排序 + 查找表存放num出现的次数
## 时间复杂度：O（n^2）
## 空间复杂度：O(n)
def threeSum1( nums: List[int]) -> List[List[int]]:
    nums.sort()  # 先对nums数组排序，防止之后查找出现重复
    
    res = []
    nums_counter = {}
    for i in range(len(nums)):
        # if nums_counter.get(nums[i])!=None:
        #     nums_counter[nums[i]] += 1
        # else:
        #     nums_counter[nums[i]] = 1
        nums_counter[nums[i]] = nums_counter.get(nums[i],0) + 1
    nums = np.unique(nums)
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]*2+nums[j]==0 and nums_counter[nums[i]]>=2:
                res.append([nums[i],nums[i],nums[j]])
            elif nums[i]+nums[j]*2==0 and nums_counter[nums[j]]>=2:
                res.append([nums[i],nums[j],nums[j]])
            else:
                t = 0 - nums[i] - nums[j]
                if nums_counter.get(t)!=None and t>nums[j]:
                    res.append([nums[i],nums[j],t])
    return res

## 2. 排序 + 双指针
## 时间复杂度：O（n^2） 
## 空间复杂度：O(1)
def threeSum2( nums: List[int]) -> List[List[int]]:
    def next_number_index(nums,index):
        if index >= len(nums):
            return len(nums)
        for i in range(index+1,len(nums)):
            if nums[i] != nums[index]:
                return i
        return len(nums)
    def pre_number_index(nums,index):
        if index < 0:
            return -1
        for i in range(index-1,-1,-1):
            if nums[i] != nums[index]:
                return i
        return -1
    nums.sort()  # 先对nums数组排序，防止之后查找出现重复
    res = []
    index = 0
    while index < len(nums):
        if nums[index] > 0:
            break
        l = index + 1
        r = len(nums) - 1
        while l < r:
            if nums[index] + nums[l] + nums[r] == 0:
                res.append([nums[index],nums[l],nums[r]])
                l = next_number_index(nums,l)
                r = pre_number_index(nums,r)
            elif nums[index] + nums[l] + nums[r] > 0:
                r = pre_number_index(nums,r)
            else:
                l = next_number_index(nums,l)
        index = next_number_index(nums,index)
    return res

# nums = [-1,0,1,0]
nums = [-1,0,1,2,-1,-4]
res = threeSum2(nums)
res

