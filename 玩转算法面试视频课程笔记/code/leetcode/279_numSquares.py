from collections import deque
from typing import List

def numSquares1(n: int) -> int:
    if n == 0: return 0
    queue = deque([n])
    step = 0
    visited = set()
    while(queue):
        step+=1
        for _ in range(len(queue)):
            tmp=queue.pop()
            for i in range(1,int(tmp**0.5)+1):
                x=tmp-i**2

                if(x==0):
                    return step
                if(x not in visited):
                    queue.appendleft(x)
                    visited.add(x)
    return step

def numSquares2(n: int) -> int:
    dp=[i for i in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,int(i**(0.5))+1):
            dp[i]=min(dp[i],dp[i-j*j]+1)
    return dp[-1]

res = numSquares1(n=12)



