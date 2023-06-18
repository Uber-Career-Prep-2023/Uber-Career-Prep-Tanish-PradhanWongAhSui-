# Generic traversal
# Time complexity- O(V+E)
# Space complexity - O(V+E)

def RoadNetworks(towns: list[str], roads: list) -> int:
    # convert to adjcency list graph

    # loop through with dfs and everytime 
    # it starts a new iteration and it hasn't been visited
    # increment count by 1

    count = 0
    visited = set()

    graph = {}
    for town1, town2 in roads:
        if town1 not in graph:
            graph[town1] = set()
        if town2 not in graph:
            graph[town2] = set()
        graph[town1].add(town2)
        graph[town2].add(town1)

    def dfs(vertex: str):
        visited.add(vertex)
        for neighbor in graph.get(vertex):
            if neighbor not in visited:
                dfs(neighbor)

    for town in towns:
        if town not in visited and len(graph.get(town, set())) != 0:
            count += 1
            dfs(town)
    
    return count

# test1
assert 3 == RoadNetworks(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")])
assert 2 == RoadNetworks(["Anchorage", "Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")])
assert 0 == RoadNetworks([], [])
assert 0 == RoadNetworks(["Gangtok", "Siliguri", "Delhi", "Mumbai"], [])
assert 2 == RoadNetworks(["Gangtok", "Siliguri", "Delhi", "Mumbai", "Anchorage", "Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")])
assert 0 == RoadNetworks([], [("A", "B"), ("C", "D")])
assert 0 == RoadNetworks(["A", "B", "C"], [])
assert 1 == RoadNetworks(["A", "B", "C"], [("A", "B"), ("B", "C"), ("A", "B"), ("B", "C")])
assert 1 == RoadNetworks(["A", "B", "C"], [("A", "B"), ("B", "C"), ("C", "C")])


# took 32 minutes