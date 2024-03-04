# import sys
# input = sys.stdin.readline

# computer = int(input())
# n = int(input())
# virus = set([1])
# result = 0

# # 그래프 탐색 알고리즘을 써야할듯
# for i in range(n):
#     chain = set(map(int, input().split()))
#     # 이미 바이러스에 걸려있을 경우 제외
#     m = virus & chain
#     if m and len(m) != 2:
#         virus.update(chain)
#         result += 1

# print(result)

computer = int(input())
n = int(input())
graph = [[] for i in range(computer+1)]
result = 0

# 각 연관관계가 정의된 그래프
for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i, visited)
    return visited

print(len(dfs(1))-1)




