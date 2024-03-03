import sys
input = sys.stdin.readline

c = int(input())  # 컴퓨터 수
p = int(input())  # 직접 연결되어 있는 컴퓨터 쌍의 수
count = 0
visited = [False]*(c+1)
graph = [[] for _ in range(c+1)]
for i in range(p):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)


def dfs(v):
    global count
    visited[v] = True
    for j in graph[v]:
        if not visited[j]:
            visited[j] = True
            count += 1
            dfs(j)

dfs(1)
print(count)