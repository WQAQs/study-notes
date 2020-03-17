from typing import List

## 1. sort+双指针
def threeSumClosest(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return None
    nums.sort()
    diff = abs(nums[0] + nums[1] + nums[2] - target)
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        t = target - nums[i]
        while l < r:
            if nums[l] + nums[r] == t:
                return target
            else:
                if abs(nums[l] + nums[r] + nums[i] - target) < diff:
                    diff = abs(nums[l] + nums[r] + nums[i] - target)
                    res = nums[l] + nums[r] + nums[i]
                if nums[l] + nums[r] < t:
                    l += 1
                else:
                    r -= 1
    return res
nums = [0,2,1,-3]
target = 1
res = threeSumClosest(nums, target)
res