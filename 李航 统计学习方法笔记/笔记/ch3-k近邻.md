**k-d树搜索伪代码**：
```python

'''
k-d树中搜索最近邻点
输入：k-d树根节点root，要查询的结点target
输出：k-d树中距离target最近的结点nearest_node
'''
def kdsearch_nearest(root, target):
    ## 1. 进行二叉查找，建立搜索路径，直到找到一个叶结点
    #二分查找target结点应该落在哪个区域
    if root == NULL:
        return
    cur_node = root
    while cur_node != NULL:
        search_stack.push(cur_node)#把cur_node压入堆栈
        ##更新cur_node
        s = cur_node->split_dim #当前结点划分区域的维度
        if target->val[s] < cur_node->val[s]: 
            cur_node = cur_node->left
        else:
            cur_node = cur_node->right
    ## 2. 把叶结点设为在root为根的树中的初始最近邻点i_nearest_node
    i_nearest_node = search_stack.pop() #弹出搜索堆栈放进的最后一个结点，即一个叶结点
    if nearest_dis > dis(i_nearest_node,taget): #比较，更新全局最近邻点nearest_node
        nesrest_node = i_nearest_node
        nearest_dis > dis(i_nearest_node,taget)
    ## 3. 回溯更新全局最近邻点nearest_node
    while search_stack != NULL:
        cur_node = search_stack.pop()
        s = cur_node->split_dim
        if target[s] <= cur_node[s]: # 如果taget位于它的父结点的左区域，那么另外一个区域为右区域，
            search(cur_node->right,target) # 进入右区域递归搜寻最近邻点
        else: # 如果taget位于它的父结点的右区域，那么另外一个区域为左区域，
            search(cur_node->left,target) # 进入左区域递归搜寻最近邻点
        if dis(cur_node->right,taget) < nearest_dis: # 计算cur_node到target的距离，比较，更新最近邻点
            nearest_node = cur_node
            nearest_dis = dis(cur_node,target)
    return # 回退到根节点时，即search_stack弹出最底下的root结点，
           # 在root为根的树中结束搜索最近邻点，返回

## 使用k-d树搜索函数
    nearest_dis = 无穷大
    nearest_node = Node(0)
    kdsearch_nearest(root, target)
```

