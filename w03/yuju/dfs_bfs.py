from collections import deque

# 1. 스택을 활용한 DFS 구현
def dfs_stack(graph, start):
    stack = [start]                       # 시작 노드를 스택에 추가
    visited = [False] * (len(graph) + 1)  # 방문 여부를 저장하는 리스트
    
    while stack:                # 스택이 빌 때까지 반복
        node = stack.pop()      # 현재 방문하고 있는 노드를 꺼냄
        visited[node] = True    # 방문 체크 후
        print(node, end=' ')    # 출력

        # 스택에 역순으로 인접 노드를 추가
        for neighbor in reversed(graph[node]):  # 현재 노드와 연결된 인접 노드 중
            if visited[neighbor] is False:      # 방문하지 않은 노드(다음에 방문할 노드)를
                stack.append(neighbor)          # 스택에 추가

        # extend로 line 14~16 코드 간소화
        # stack.extend(neighbor for neighbor in reversed(graph[node]) if not visited[neighbor])


# 2. 재귀를 활용한 DFS 구현
def dfs_recursive(graph, current_node, visited=None):
    if visited is None:                       # 처음 호출 시에만
        visited = [False] * (len(graph) + 1)  # 방문 여부를 저장하는 리스트 초기화
    
    visited[current_node] = True    # 현재 노드를 방문했다고 표시
    print(current_node, end=' ')    # 현재 노드 출력

    for neighbor in graph[current_node]:              # 현재 노드와 연결된 인접 노드 중
        if visited[neighbor] is False:                # 방문하지 않은 노드(다음에 방문할 노드)에 대해
            dfs_recursive(graph, neighbor, visited)   # dfs_recursive 함수를 재귀 호출


# 3. 큐를 활용한 BFS 구현
def bfs(graph, start):
    queue = deque([start])                   # 시작 노드를 큐에 추가
    visited = [False] * (len(graph) + 1)     # 방문 여부를 저장하는 리스트
    
    while queue:                # 큐가 빌 때까지 반복
        node = queue.popleft()  # 현재 방문하고 있는 노드를 꺼내고,
        visited[node] = True    # 방문 체크 후
        print(node, end=' ')    # 출력
        
        for neighbor in graph[node]:          # 현재 노드와 연결된 인접 노드 중
            if visited[neighbor] is False:    # 방문하지 않은 노드(다음에 방문할 노드)를
                queue.append(neighbor)        # 큐에 추가
        
        # extend로 line 45~47 코드 간소화        
        # queue.extend(neighbor for neighbor in graph[node] if not visited[neighbor])


# 예시 그래프
graph = {
    1: [2, 3],                #     1
    2: [1, 4, 5],             #    / \
    3: [1],                   #   2   3
    4: [2],                   #   | \
    5: [2]                    #   4   5
}

# 함수 실행
print("DFS by Stack:", end=' ')
dfs_stack(graph, 1)
print("\nDFS by Recursive:", end=' ')
dfs_recursive(graph, 1)
print("\nBFS:", end=' ')
bfs(graph, 1)