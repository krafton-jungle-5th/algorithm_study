n, m = map(int, input().split())


visited = [False for _ in range(0,n)]
lst = [i for i in range(1,n+1)]
container = []

def dfs(idx):
    global m

    if (idx == m):
        for i in container:
            print(i, end=" ")
        print("")
    for i in range(0,n):
        if not visited[i]:
            visited[i]=True
            container.append(lst[i])
            dfs(idx+1)
            container.pop()
            visited[i]=False

dfs(0)