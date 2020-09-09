class Solution:
    '''
    题目：一个长度为N的数组，其中的元素取值范围是1到N，要求快速判断数组是否存在重复数字
    !!!!!注意：和leetcode 中的217题不一样，这里限制了“一个长度为N的数组，其中的元素取值范围是1到N”，
    leetcode上的没有这个限制条件，那么用这个代码就会出现输入例如nums = [1, 2, 3, 4, 6]，
    !!!!!!出现错误IndexError: list index out of range
    '''

## 1.set查找表
def containsDuplicate(self, nums):
    nums_set = set()
    for x in nums:
        if x in nums_set:
            return True
        else:
            nums_set.add(x)
    return False
so = Solution()
nums = [1, 2, 3, 4, 6]
res = so.containsDuplicate(nums)
res


