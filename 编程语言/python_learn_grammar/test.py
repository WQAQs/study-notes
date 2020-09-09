import heapq
nums = [1,3,2,6,3]
h = []
def heap_create(h,nums): # 创建heap
    for x in nums:
        heapq.heappush(h, x)
    
heap_create(h,nums)
h  # h:[2,3,3,7,6]  
res = heapq.heappop(h) #弹出最小堆h中的堆顶元素，即最小元素
res # res:[3,3,6,7] 注意！！:在弹出h中的堆顶元素之后，h的变化，
    #                        因为最小堆底层是由二叉树实现的
## 可以用索引访问最小堆h中的元素
i0 = h[0] #i0:3
i2 = h[3] #i2:6```