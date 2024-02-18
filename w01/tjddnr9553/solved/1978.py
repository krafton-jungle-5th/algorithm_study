import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True


def solution():
    count = 0
    N = int(input())
    num_list = list(map(int, input().split()))
    for j in num_list:
        if is_prime(j):
            count += 1

    print(count)


solution()
