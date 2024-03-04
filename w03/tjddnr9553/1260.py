import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)


dfs(v)

visited = [False]*(n+1)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        k = q.popleft()
        print(k, end=' ')
        for i in sorted(graph[k]):
            if not visited[i]:
                visited[i] = True
                q.append(i)


print()
bfs(v)
