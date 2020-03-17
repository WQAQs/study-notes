## 不存在无限不循环的情况
## 如果出现重复的数就会陷入死循环，返回false。
## 当出现1，就返回true
def isHappy(self, n: int) -> bool:
    issame = [n]
    while n != 1:
        a = str(n)
        n = 0
        for c in a:
            n += pow(int(c),2)
        issame.append(n)
        if len(issame) != len(set(issame)):  # 使用set检查是否出现重复数字
            return False
    return True

## 思路同上只是优化了下检查重复数字，计算和
def isHappy(self, n: int) -> bool:
    def op(n):
        sum = 0
        while n > 0:
            sum += (n % 10)*(n % 10)
            # sum += pow(n%10,2)  比较耗时
            n = n // 10  ## 注意！！！这里要使用整除号// 否则就错啦！！！
        return sum
    setn = set()
    while n != 1:
        n = op(n)
        if n in setn:
            return False
        else:
            setn.add(n)
    return True
    

