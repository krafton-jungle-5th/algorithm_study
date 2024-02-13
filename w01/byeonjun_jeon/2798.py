import math
from itertools import *

n, m = map(int, input().split(" "))

numArr = list(map(int, input().split(" ")))

resultArr = list(combinations(numArr, 3))

bench = math.inf

result = 0

# m값 - sum(i)의 절대값이 적으면 저장
for i in resultArr:
    total = sum(i)
    if total <= m and m-total < bench:
        result = total
        bench = m-total

print(result)
