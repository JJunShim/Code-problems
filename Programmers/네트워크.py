def dfs(node, computers, visited):
    visited[node] = True
    for i, neighbor in enumerate(computers[node]):
        if not visited[i] and neighbor and i != node:
            visited = dfs(i, computers, visited)
    return visited


def solution(n, computers):
    answer, node = [0] * 2
    visited = [False] * n
    while not all(visited):
        node = visited.index(False)
        answer += 1
        visited = dfs(node, computers, visited)
    return answer
