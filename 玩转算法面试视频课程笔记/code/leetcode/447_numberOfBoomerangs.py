## Using Hash Map
## Time Complexity: O(n^2)
## Space Complexity: O(n)
import math 
from typing import List

def numberOfBoomerangs(points: List[List[int]]) -> int:
    res = 0
    def dis(a,b): ## 计算距离时不进行开根运算, 以保证精度!!
        return (a[0] - b[0])*(a[0] - b[0])+(a[1]-b[1])*(a[1]-b[1])
    for i in range(len(points)):
        record = {}
        j = 0
        while j < len(points):
            if j != i:
                d = dis(points[i],points[j])
                record[d] = record.get(d,0) + 1
            j += 1
        for key in record:
            res += record[key]*(record[key]-1)
    return res

points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
res = numberOfBoomerangs(points)
res

