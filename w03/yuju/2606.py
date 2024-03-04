n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited) - 1)