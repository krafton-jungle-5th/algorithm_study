import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations
import copy

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(tmp_lab):
    queue = deque()
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

def make_wall_combinations():
    wall_combinations = combinations(empty, 3)

    for walls in wall_combinations:
        tmp_lab = copy.deepcopy(lab)

        for wall in walls:
            tmp_lab[wall[0]][wall[1]] = 1

        bfs(tmp_lab)

x, y = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(x)]
empty = [(i, j) for i in range(x) for j in range(y) if lab[i][j] == 0]

result = 0
make_wall_combinations()

print(result)
