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

x = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
y = adjacencySet(x)
for i in y:
    print(i, y[i])

from collections import deque

def bfs(target: int, graph: dict) -> bool:
    # Time - O(V+E)
    # Space - O(V)
    visited = [False] * len(graph)
    queue = deque()

    source = 0 # Assuming source of vertex is 0
    queue.append(source)

    while queue:
        vertex = queue.popleft()
        visited[vertex] = True
        if vertex == target:
            return True
        for neighbor in graph.get(vertex, set()):
            if not visited[neighbor]:
                queue.append(neighbor)
    return False

            
def dfs(target: int, graph: dict) -> bool:
    # Time - O(V+E)
    # Space - O(V)
    visited = [False] * len(graph)

    def recursive_dfs(vertex: int) -> bool:
        visited[vertex] = True
        if vertex == target:
            return True
        
        for neighbor in graph.get(vertex, set()):
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False
    
    return recursive_dfs(0) # Assuming source of vertex is 0 and assuming the graph is undirected and connected

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

