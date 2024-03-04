import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def dfs(v, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i, visited)
    return visited

def bfs(v, visited=[]):
    visited.append(v)
    queue = deque([v])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

print(*dfs(v))
print(*bfs(v))
