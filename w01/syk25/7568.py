N = int(input())
people = []
rank = []

for i in range(N):
    weight_height = list(map(int, input().split()))
    people.append(weight_height)
    rank.append(1)

for i in range(N):
    for j in range(N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1

print(*rank)
