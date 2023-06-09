from collections import deque
import math

def alternatingpath(edges: list, origin, destination) -> int:
    # building adjacency list
    graph = {}
    for vertex1, vertex2, weight in edges:
        if vertex1 not in graph:
            graph[vertex1] = set()
        if vertex2 not in graph:
            graph[vertex2] = set()
        graph[vertex1].add((vertex2, weight))
    min_dist = math.inf
    # bfs traversal
    queue = deque([(vertex1, "", 0)])
    while queue:
        curr, last, count = queue.pop()
        count += 1
        if count >= min_dist:
            continue
        if curr == destination:
            min_dist = count
            continue
        for next_vertex, weight in graph.get(curr, set()):
            if weight != last:
                queue.append((next_vertex, weight, count))
    return min_dist

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"

alternatingpath([(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"), (C, B, "red"), (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")], A, E)

# took 25 minutes so far
