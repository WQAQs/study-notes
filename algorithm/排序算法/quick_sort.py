def quick_sort(nums,start,end):
    if start >= end:  # 递归结束的条件！！！！！！！
        return
    left = start
    right = end
    key = nums[start]  # 此时，已经在nums[start]位置留下了一个坑
    ## 1. 划分：
    ##    把nums[left,right]范围内的数，比key小的放在左边，比key大的放在右边
    ## 从右到左，直到找到比key大的元素，去填前面留下的一个坑
    while left < right:
        while left < right and nums[right] >= key:
            right -= 1
        nums[left] = nums[right]  # 找到比key小的数，去填前面nums[left]留下的坑
        while left < right and nums[left] < key:
            left += 1
        nums[right] = nums[left] # 找到比key大的数，去填前面nums[right]留下的坑
    nums[left] = key # 此时left==right,把key放好
    ## 2.递归调用:
    ##   分别对左边的子数组，右边的子数组快排
    quick_sort(nums,start,left-1)
    quick_sort(nums,left+1,end)

nums = [2,3,1,6,4,2,2]
quick_sort(nums,0,len(nums)-1)
nums