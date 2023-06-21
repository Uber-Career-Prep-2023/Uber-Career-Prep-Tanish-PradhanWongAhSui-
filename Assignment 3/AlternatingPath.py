# technique used is bfs graph traversal
# time complexity - O(V+E)
# space complexity - O(V+E)

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
    queue = deque([(origin, "", 0)])
    while queue:
        curr, last, count = queue.pop()
        if count >= min_dist:
            continue
        if curr == destination:
            min_dist = count
            continue
        count += 1
        for next_vertex, weight in graph.get(curr, set()):
            if weight != last:
                queue.append((next_vertex, weight, count))
    if min_dist == math.inf:
        return -1
    return min_dist

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"

assert alternatingpath(
    [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"),
     ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")],
    "A", "E"
) == 4

assert alternatingpath(
    [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"),
     ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")],
    "E", "D"
) == -1

assert alternatingpath(
    [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"),
     ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")],
    "C", "E"
) == 2

assert alternatingpath(
    [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"),
     ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")],
    "E", "B"
) == -1

assert alternatingpath([], "A", "E") == -1

assert alternatingpath([("A", "A", "blue")], "A", "A") == 0

assert alternatingpath([("A", "B", "blue"), ("B", "C", "red"), ("C", "D", "blue")], "A", "E") == -1

assert alternatingpath([("A", "B", "blue")], "A", "B") == 1

assert alternatingpath(
    [("A", "B", "blue"), ("B", "C", "red"), ("C", "D", "blue"), ("D", "E", "red")],
    "A", "E"
) == 4

assert alternatingpath(
    [("A", "B", "blue"), ("B", "C", "blue"), ("C", "D", "blue"), ("D", "E", "red")],
    "A", "E"
) == -1

assert alternatingpath(
    [("A", "B", "blue"), ("B", "C", "red"), ("C", "D", "blue"), ("D", "E", "red")],
    "E", "A"
) == -1


# took 34 minutes