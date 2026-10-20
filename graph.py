from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
def dfs(graph, start):
    visited = {start}
    stack = [start]            # ← list 当栈
    result = []

    while stack:
        node = stack.pop()     # ← 注意：没有 0，从末尾取
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

bfs(graph, 'A')
print(bfs(graph, "A"))
print(dfs(graph, "A"))       # ← 这个

