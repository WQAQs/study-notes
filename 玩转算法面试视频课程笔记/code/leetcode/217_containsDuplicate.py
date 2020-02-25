class Solution:
    '''
    题目：一个长度为N的数组，其中的元素取值范围是1到N，要求快速判断数组是否存在重复数字
    !!!!!注意：和leetcode 中的217题不一样，这里限制了“一个长度为N的数组，其中的元素取值范围是1到N”，
    leetcode上的没有这个限制条件，那么用这个代码就会出现输入例如nums = [1, 2, 3, 4, 6]，
    !!!!!!出现错误IndexError: list index out of range

    分析：
   解法1：如果N个元素的范围都是在1到N，所以如果没有重复元素，则每一个位置恰好可以对应数组中的一个元素之，通过将当前元素k交换到其本身应该在的位 置k，也就是k=array[i], array[array[i］，并判断是否存在duplication或者已经就绪。时间复杂度O(N)，空间复杂度O(1)；
   解法2：由于元素取值范围确定，可以使用BitMap将数组元素映射到对应的位置，如果一个位置对应了两个元素，则有重复。时间复杂度和空间复杂度都是O(N)；
   解法3：先排序，O(NlogN)，然后比较相邻元素是否相等，O(N)；
    '''
    def containsDuplicate(self, nums):
        def has_dup(nums, cur):
            if len(nums) == 0 or cur == len(nums):
                return False
            if nums[cur] == cur:
                cur += 1
                return has_dup(nums, cur)
            elif nums[cur] == nums[nums[cur]]:
                return True
            else:
                temp = nums[cur]
                nums[cur] = nums[temp]
                nums[temp] = temp
                return has_dup(nums, cur)
        res = has_dup(nums, 0)
        return res

so = Solution()
nums = [1, 2, 3, 4, 6]
res = so.containsDuplicate(nums)
res


