from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

result = float('inf')
houses = []
chicken_list = []

def chicken_dist(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chicken_list.append([i, j])
            
for chicken in combinations(chicken_list, m):
    sum_distance = 0
    for house in houses:
        distance = float('inf')
        for j in range(m):
            distance = min(distance, chicken_dist(house, chicken[j]))
        sum_distance += distance
    result = min(result, sum_distance)
    
print(result)