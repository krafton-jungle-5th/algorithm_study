import sys
sys.setrecursionlimit(10**6)

n = int(input())
parents = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, parent):
    parents[v] = parent
    for i in graph[v]:
        if parents[i] == 0:
            dfs(i, v)


dfs(1, 0)

for i in range(2, n+1):
    print(parents[i])