import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

def bfs():
    ans = 1
    for i in graph:
        for j in i:
            print(graph[i][j])

# bfs()


