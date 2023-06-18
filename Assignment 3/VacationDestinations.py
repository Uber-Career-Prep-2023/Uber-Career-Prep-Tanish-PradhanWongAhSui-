from collections import deque
# bfs traversal is used
# time complexity - O(V+E)
# space complexity - O(V+E)

def numdestinations(flights: list, origin: str, k: float) -> list:
    destinations = set()
    graph = {}
    for place1, place2, time in flights:
        if place1 not in graph:
            graph[place1] = set()
        if place2 not in graph:
            graph[place2] = set()
        graph[place1].add((place2, time))
        graph[place2].add((place1, time))

    # bfs works better than dfs in this case
    queue = deque(graph.get(origin, set()))
    while queue:
        city, time = queue.popleft()
        if city in destinations:
            continue
        if time <= k and city != origin:
            destinations.add(city)
            for next_place in graph.get(city):
                queue.append((next_place[0], next_place[1]+time+1))
    
    return len(destinations)

assert 2 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", 5)
assert 4 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", 7)
assert 6 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", 8)
assert 6 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", 200000)
assert 0 == numdestinations([("Philadelphia", "Washington, D.C.", 2.5)], "New York", 10000)
assert 0 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", 00000)
assert 0 == numdestinations([], "", 10000)
assert 0 == numdestinations([], "", -100)
assert 0 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", -200000)
assert 1 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "New York", 3)
assert 3 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "Boston", 4)
assert 2 == numdestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)], "Boston", 3)

# took 30 minutes