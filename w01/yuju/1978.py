count = int(input())
values = map(int, input().split())
prime_count = 0

def is_prime(num):
    if num == 1:
        return False         
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in values:
    if is_prime(num):
        prime_count += 1
        
print(prime_count)