n = int(input())
x_list = list(map(int, input().split()))
x_set = sorted(set(x_list))

dictionary = {x_set[i] : i for i in range(len(x_set))}

for key in x_list:
    print(dictionary[key], end = ' ')