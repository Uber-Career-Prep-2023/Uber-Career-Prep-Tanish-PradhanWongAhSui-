# Build an Adjacency List/Set Representation of a Graph

def adjacencySet(edges: list)-> dict:
    # Time - O(E)
    # Space - O(V+E)
    res = {}
    for u, v in edges:
        if u not in res:
            res[u] = set()
        if v not in res:
            res[v] = set()
        res[u].add(v)
    return res

from collections import deque

def bfs(target: int, graph: dict) -> bool:
    # Time - O(V+E)
    # Space - O(V)

    visited = set()
    for vertex in graph:
        if vertex in visited:
            continue
        queue = deque([vertex])
        while queue:
            curr = queue.popleft()
            if curr == target:
                return True
            visited.add(curr)
            for neighbor in graph.get(curr, set()):
                if neighbor not in visited:
                    queue.append(neighbor)
    return False

def dfs(target: int, graph: dict) -> bool:
    # Time - O(V+E)
    # Space - O(V)

    visited = set()
    def dfs(vertex: int) -> bool:
        visited.add(vertex)
        if vertex == target:
            return True
        for next in graph.get(vertex, set()):
            if next not in visited:
                return dfs(next)
        return False

    for vertex in graph:
        if vertex in visited:
            continue
        if dfs(vertex):
            return True
    return False

def topologicalSortDFS(graph: dict) -> list:
    # Time - O(V+E)
    # Space - O(V)
    stack = []
    visited = [False] * len(graph)
    
    def recursiveTSDFS(vertex: int):
        visited[vertex] = True
        for neighbor in graph.get(vertex, set()):
            if not visited[neighbor]:
                recursiveTSDFS(neighbor)
        stack.append(vertex)

    for vertex in graph:
        recursiveTSDFS(vertex)
    return stack[::-1]


def topologicalSortKahn(graph: dict) -> list:
    # Time - O(V+E)
    # Space - O(V)
    res = []

    indegree = [0] * len(graph)
    for source in graph:
        for dest in graph.get(source, set()):
            indegree[dest] += 1

    queue = deque()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            res.append(i)
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex, set()):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                res.append(neighbor)
    return res

