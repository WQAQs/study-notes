'''
451. 根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
'''
def frequencySort(s: str) -> str:
    s_list = sorted(set(s),key = lambda x: s.count(x), reverse = True) # 注意这里使用key以及lambda的用法
    ## key表示比较的函数(即比较大小的规则)，每一次把待排序数（即set（s）中的一项）使用该规则进行排序，
    ## reverse设置是否逆序返回，逆序表示从大到小的顺序，默认的顺序是从小到大
                # y = lambda x: s.count(x) #这里y是一个lambda函数
                # for x in s:
                #     t = y(x) #调用y函数，返回一个结果
    return "".join(c*s.count(c) for c in s_list) # 注意列表操作*表示重复元素

s = "11222234"
frequencySort(s)