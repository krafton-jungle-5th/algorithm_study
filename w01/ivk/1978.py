n = int(input())

numbers = list(map(int, input().split()))
cnt = 0

# Sol 1
for num in numbers:
    if num != 1:
        for i in range(2, int(num ** 1/2)+1):
            if num % i == 0:
                break
        else:
            cnt += 1


# Sol 2            
numbers = list(map(int, input().split()))
cnt = sum(num != 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) for num in numbers)

print(cnt)
            