import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
visited = [False]*(n+1)
answer = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(k):
    visited[k] = True
    for j in sorted(graph[k]):
        if not visited[j]:
            answer[j] = k
            dfs(j)


dfs(1)
for l in range(2, n+1):
    print(answer[l])
