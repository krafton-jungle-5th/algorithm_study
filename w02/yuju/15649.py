from itertools import permutations

n, m = map(int, input().split())

n_list = [i+1 for i in range(n)]
per = permutations(n_list, m)  

for result in per:
    print(*result)  