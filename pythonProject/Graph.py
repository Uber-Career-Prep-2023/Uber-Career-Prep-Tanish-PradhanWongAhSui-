from collections import deque


def adjacencySet(edges: list) -> dict:
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = set()
        graph[edge[0]].add(edge[1])
    return graph


def bfs(target: int, graph: dict) -> bool:
    # assuming it is a completely connected graph and 0 is the source of the bfs
    # assuming a target and a non-empty graph is given
    queue = deque([0])
    visited = set([0])
    while queue:
        curr = queue.popleft()
        if curr == target:
            return True
        for next_v in graph.get(curr, set()):
            if next_v not in visited:
                visited.add(next_v)
                queue.append(next_v)
    return False


def dfs(target: int, graph: dict) -> bool:
    # assuming it is a completely connected graph and 0 is the source of the bfs
    # assuming a target and a non-empty graph is given
    visited = set()

    def dfs_recursive(vertex: int):
        visited.add(vertex)
        if vertex == target:
            return True
        for next_v in graph.get(vertex, set()):
            if next_v in visited:
                continue
            return dfs_recursive(next_v)
        return False
    return dfs_recursive(0)


def dfs_iterative(target: int, graph: dict) -> bool:
    # assuming it is a completely connected graph and 0 is the source of the bfs
    # assuming a target and a non-empty graph is given
    visited = set()
    stack = [0]
    while stack:
        curr = stack.pop()
        if curr == target:
            return True
        visited.add(curr)
        for next_v in graph.get(curr, set()):
            if next_v not in visited:
                stack.append(next_v)
    return False


def topologicalSort_dfs(graph: dict) -> list:
    res = []
    visited = set()

    def dfsT(node: int):
        visited.add(node)
        for next_v in graph.get(node, set()):
            if next_v not in visited:
                dfsT(next_v)
        res.append(node)
    for node in graph:
        if node not in visited:
            dfsT(node)
    return res[::-1]


def topologicalSort_Kahns(graph: dict) -> list:
    # assumes that the input graph is a valid directed acyclic graph (DAG) and does not check for cycles
    indegree = {}
    for vertex in graph:
        indegree[vertex] = len(graph[vertex])
    queue = deque()
    for vertex in indegree:
        if indegree[vertex] == 0:
            queue.append(vertex)
    res = []
    while queue:
        curr = queue.popleft()
        res.append(curr)
        for next_v in graph.get(curr):
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                queue.append(next_v)
    return res




