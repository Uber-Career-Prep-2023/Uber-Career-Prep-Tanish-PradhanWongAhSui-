from collections import deque

def precourses(courses: list, map: dict) -> list:
    # Time - O(V+E)
    # Space - O(V +E)
    graph = {}
    for course in courses:
        graph[course] = set()
    for course2 in map:
        for prereq in map[course2]:
            graph.get(prereq, set()).add(course2)
    res = []

    # topological sort

    # modified dfs

    # stack = []
    # visited = {}
    # for course in graph:
    #     visited[course] = False
    # for vertex in graph:
    #     pass
    # def dfs(vertex: str):
        
    # kahn's algorithm

    indegree = {}
    queue = deque()
    for course in graph:
        indegree[course] = len(map.get(course, set()))
    for course in indegree:
        if indegree[course] == 0:
            queue.append(course)
    
    while queue:
        vertex = queue.popleft()
        res.append(vertex)
        for neighbor in graph.get(vertex, set()):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return res
            

assert ['Intro to Programming',
 'Data Structures',
 'Advanced Algorithms',
 'Databases',
 'Operating Systems'] == precourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] })
assert ['Intro to Writing',
 'Plays & Screenplays',
 'Contemporary Literature',
 'Ancient Literature',
 'Comparative Literature'] == precourses(["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] })
assert precourses([], {}) == []

# took 20 minutes