from typing import List

## 1. 基于桶
def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    if t < 0:
        return False;
    bucket = {}
    w = t + 1
    def getid(x,w):
        return x//w 
    for i in range(len(nums)):
        if bucket.get(getid(nums[i],w)) != None:
            return True
        if bucket.get(getid(nums[i],w)-1) != None and\
            bucket.get(getid(nums[i],w)-1) >= nums[i] - t:
            return True
        if bucket.get(getid(nums[i],w)+1) != None and\
            bucket.get(getid(nums[i],w)+1) <= nums[i] + t:
            return True
        bucket[getid(nums[i],w)] = nums[i]
        if len(bucket) > k:
            bucket.pop(getid(nums[i-k],w))
    return False
            
res = containsNearbyAlmostDuplicate([-1,-1],1,-1)
res


