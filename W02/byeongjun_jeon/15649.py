import sys
input = sys.stdin.readline

n, m = map(int, input().split())
append_arr = []

def dfs():

    if len(append_arr) == m:
        print(*append_arr)
        return

    for i in range(1, n+1):
        if i not in append_arr:
            append_arr.append(i)
            dfs()
            append_arr.pop()

dfs()
