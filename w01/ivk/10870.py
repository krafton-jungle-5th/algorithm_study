n = int(input())

# Sol 1
ans = 0
arr = [0, 1]

if n >= 1:
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
ans = arr[n]

# Sol 2
if n <= 1:
    ans = n
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    ans = b

print(ans)
    
    
        
        

