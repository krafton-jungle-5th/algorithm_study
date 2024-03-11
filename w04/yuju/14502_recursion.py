# 시간 초과
import sys
input = sys.stdin.readline

from collections import deque
import copy

d = [[-1,0], [1,0], [0,-1], [0,1]]

def bfs():
    queue = deque()
    tmp_lab = copy.deepcopy(lab)
    for i in range(x):
        for j in range(y):
            if tmp_lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        virus_x, virus_y = queue.popleft()
        
        for i in range(4):
            infection_x = virus_x + d[i][0]
            infection_y = virus_y + d[i][1]
            
            if (0 <= infection_x < x) and (0 <= infection_y < y):
                if tmp_lab[infection_x][infection_y] == 0:
                    tmp_lab[infection_x][infection_y] = 2
                    queue.append((infection_x, infection_y))
                    
    global result
    count = 0
    for i in range(x):
        for j in range(y):
            if tmp_lab[i][j] == 0:
                count += 1
                
    result = max(result, count)

def make_wall_recursion(count):
    if count == 3:
        bfs()
        return
    for i in range(x):
        for j in range(y):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall_recursion(count+1)
                lab[i][j] = 0
                
x, y = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(x)]

result = 0
make_wall_recursion(0)

print(result)