import sys
input = sys.stdin.readline

n = int(input())
arr = []

result = []

# 풀이 참고함
for i in range(n):
    arr.append(list(map(int, input().split())))

def dfs(x,y,n):
    # 시작점의 색깔을 정의
    color = arr[x][y]
    # x 좌표와 y좌표를 n만큼 탐색
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 처음 선택한 color와 arr[i][j]의 값이 다르면 다음 탐색
            if color != arr[i][j]:
                # 각 영역을 모두 탐색
                dfs(x,y,n//2)
                dfs(x,y+n//2,n//2)
                dfs(x+n//2,y,n//2)
                dfs(x+n//2,y+n//2,n//2)
                return
    # 만약 탐색이 끝났는데 재귀가 호출이 안돼면 
    if color == 0:
        result.append(0)
    else :
        result.append(1)

dfs(0,0,n)
print(result.count(0))
print(result.count(1))

