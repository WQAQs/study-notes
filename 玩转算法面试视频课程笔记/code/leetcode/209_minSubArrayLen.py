def minSubArrayLen(s, nums):
         l = 0
         r = -1 # nums[l,...,r]为滑动窗口
         sum = 0 # 初始时候，nums[0,-1]范围内没有数，sum=0
         res = len(nums) + 1
         while l< len(nums):
            if r + 1 < len(nums) and sum < s:
               r += 1
               sum += nums[r]
            else:
               sum -= nums[l]
               l += 1
            if sum >= s:
               res = min(res, r - l + 1)
         if res == len(nums) + 1:
            return 0
         else:
            return res

if __name__ == "__main__":
    nums = [1,1,82]
    s = 82
    res = minSubArrayLen(s,nums)
    res
   #  print res