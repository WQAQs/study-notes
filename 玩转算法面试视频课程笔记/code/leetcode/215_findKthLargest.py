from typing import List
import heapq

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
            return select(nums,pivot_index+1,end,k)
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

nums = [3,2,1,5,6,4]
k = 2
res = findKthLargest3(nums,k)
k

