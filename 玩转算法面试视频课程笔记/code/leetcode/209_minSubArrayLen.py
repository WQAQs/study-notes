def minSubArrayLen(s, nums):
         l = 0
         r = -1 # nums[l,...,r]为滑动窗口
         sum = 0 # 初始时候，nums[0,-1]范围内没有数，sum=0
         n = len(nums)
         res = n + 1
         while l < n:
            if r + 1 < n and sum < s:
               r += 1
               sum += nums[r]
            else:
               sum -= nums[l]
               l += 1
            if sum >= s:
               res = min(res, r - l + 1)
         if res == n + 1:
            return 0
         else:
            return res

if __name__ == "__main__":
    nums = [1,2,3]
    s = 3
    res = min_sub_array_len(s,nums)
   #  print res