from collections import deque

def dfs(v):
    dfs_visit[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and dfs_visit[i] == 0:
            dfs(i)

def bfs(v):
    q = deque([v])
    bfs_visit[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and bfs_visit[i] == 0:
                q.append(i)
                bfs_visit[i] = 1

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
                
dfs_visit = [0] * (n+1)
bfs_visit = [0] * (n+1)

dfs(v)
print()
bfs(v)