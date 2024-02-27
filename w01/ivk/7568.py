n = int(input())

bodies = []

for i in range(n):
    bodies.append(list(map(int, input().split())))
    bodies[i].append(1)

for i in range(n):
    for j in range(n):
        if i != j:
            if bodies[i][0] < bodies[j][0] and bodies[i][1] < bodies[j][1]:
                bodies[i][2] += 1

result = [body[2] for body in bodies]

print(*result)
