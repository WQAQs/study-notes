### 缓存
class NumArray:

    def __init__(self, nums: List[int]):
        self.memory = []
        self.nums = nums
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.memory.append(sum)

    def sumRange(self, i: int, j: int) -> int:
        return self.memory[j] - self.memory[i] + self.nums[i]
