n = int(input())
coord = list(map(int, input().split()))

sorted_coord = sorted(set(coord))

coord_dict = {val : idx for idx, val in enumerate(sorted_coord)}

result = [coord_dict[i] for i in coord]

print(*result)