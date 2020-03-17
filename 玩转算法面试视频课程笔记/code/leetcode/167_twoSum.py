from typing import List
## 1.使用暴力法  ！！！超时！！！
## 时间复杂度：O(n^2)
## 空间复杂度：O(1)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i+1,j+1]
    return 0 

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

## 3.使用map查找表
## 时间复杂度：O(n)
## 空间复杂度：O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    res = []
    for i in range(len(nums)):
        nums_dict[nums[i]] = i
    for i in range(len(nums)):
        j = nums_dict.get(target-nums[i])
        if j:
            res.append(i+1)
            res.append(j+1)
            return res
    return res

## 4.使用双指针
## 时间复杂度：O(n)
## 空间复杂度：O(1)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1,r+1]
        while l < r and nums[l] + nums[r] > target:
            r -= 1
        while l < r and nums[l] + nums[r] < target:
            l += 1
    return 0

print(13/2)  # 6.5
print(13//2)  # 6
print(int(6.5))  # 6

print(-13/2)  # -6.5
print(-13//2)  # -7
print(int(-6.5))  # -6