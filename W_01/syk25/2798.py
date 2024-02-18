N, target = map(int, input().split())

numbers = [int(item) for item in input().split()]

numbers.reverse()

maximum = 0

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            temp = numbers[i] + numbers[j] + numbers[k]
            if target >= temp > maximum:
                maximum = temp

print(maximum)
