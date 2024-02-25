from itertools import permutations

n, m = map(int, input().split())

numbers = list(range(1, n + 1))

permutation_list = permutations(numbers, m)

for perm in permutation_list:
    print(*perm)
