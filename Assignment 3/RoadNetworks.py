def RoadNetworks(towns: list[str], roads: list) -> int:
    # convert to adjcency list graph

    # loop through with dfs and everytime 
    # it starts a new iteration and it hasn't been visited
    # increment count by 1
    
    # Time - O(V+E)
    # Space - O(V+E)

    count = 0
    visited = {}
    for town in towns:
        visited[town] = False

    graph = {}
    for town1, town2 in roads:
        if town1 not in graph:
            graph[town1] = set()
        if town2 not in graph:
            graph[town2] = set()
        graph[town1].add(town2)
        graph[town2].add(town1)

    def dfs(vertex: str):
        visited[vertex] = True
        for neighbor in graph.get(vertex):
            if not visited[neighbor]:
                dfs(neighbor)

    for town in graph:
        if not visited[town] and len(graph.get(town, set())) != 0:
            count += 1
            dfs(town)
    
    return count

# test1
assert 3 == RoadNetworks(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")])
assert 2 == RoadNetworks(["Anchorage", "Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")])
assert 0 == RoadNetworks([], [])
assert 0 == RoadNetworks(["Gangtok", "Siliguri", "Delhi", "Mumbai"], [])

# took 25 minutes