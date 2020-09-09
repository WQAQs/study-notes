from typing import List

## 1. 使用最大长度为k的set
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    k_set = set()
    for i in range(len(nums)):
        if nums[i] in k_set:
            return True
        k_set.add(nums[i])
        if len(k_set) > k: ## 要确保在下一次检查之前，set的大小最大为k
            k_set.remove(nums[i-k]) ## 注意这里删除的元素对应的索引
    return False
nums = [1,2,3,1,2,3]
k = 2
res = containsNearbyDuplicate(nums,k)
res