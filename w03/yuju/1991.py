def pre_order(root):
    if root != '.':
        print(root, end='')
        pre_order(graph[root][0])
        pre_order(graph[root][1])


def in_order(root):
    if root != '.':
        in_order(graph[root][0])
        print(root, end='')
        in_order(graph[root][1])


def post_order(root):
    if root != '.':
        post_order(graph[root][0])
        post_order(graph[root][1])
        print(root, end='')


n = int(input())
graph = {}

for _ in range(n):
    node, left, right = map(str, input().split())
    graph[node] = [left, right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')