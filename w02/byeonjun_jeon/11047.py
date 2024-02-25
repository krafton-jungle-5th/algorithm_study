# 헛다리 짚음 재귀로 푸는게 아닌 단순 for문으로 풀이하면 되는거였음
# import sys
# import math
# input = sys.stdin.readline

# n, total = map(int, input().split())
# coin = [int(input())for _ in range(n)].sort(reverse=True)

# result_arr = []
# result = math.inf

# def dfs(start):

#     global result

#     sum(result_arr)

#     if sum(result_arr) == total:
#         print(coin)
#         result = min(result, len(result_arr))
#         return
#     elif sum(result_arr) > total:
#         return

#     for i in range(start, n):
#         result_arr.append(coin[i])
#         dfs(start+1)
#         result_arr.pop()

# dfs(0)
# print(result)

# 시간초과
# import sys
# input = sys.stdin.readline

# n, total_price = map(int, input().split())
# coin = [int(input())for _ in range(n)]
# coin.sort(reverse=True)

# result = 0
# total_coin = 0

# for i in range(n):
#     if coin[i] <= total_price:
#         while True:
#             if total_price - coin[i] >= 0:
#                 total_price -= coin[i]
#                 result += 1
#                 if total_price == 0:
#                     print(result)
#                     quit()
#             elif total_price - coin[i] < 0:
#                 break

import sys
input = sys.stdin.readline

n, total_price = map(int, input().split())
coin = [int(input())for _ in range(n)]
coin.sort(reverse=True)

count = 0

for i in range(n):
    count += total_price // coin[i]
    total_price = total_price % coin[i]

print(count)
            




