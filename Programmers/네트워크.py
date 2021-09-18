def dfs(node: int, computers: list, visited: list) -> list:
    visited[node] = True
    for i, neighbor in enumerate(computers[node]):
        if not visited[i] and i != node and neighbor:
            visited = dfs(i, computers, visited)
    return visited


def solution(n: int, computers: list) -> int:
    visited = [False] * n
    answer = 0
    while not all(visited):
        visited = dfs(visited.index(False), computers, visited)
        answer += 1
    return answer
