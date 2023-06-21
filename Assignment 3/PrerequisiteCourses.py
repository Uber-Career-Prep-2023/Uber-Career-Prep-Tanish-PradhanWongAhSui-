from collections import deque
# technique used is topological sort - kahn's algorithm
# Time complexity - O(V+E)
# Space complexity - O(V +E)

def precourses(courses: list, map: dict) -> list:
    
    graph = {}
    for course in courses:
        graph[course] = set()
    for course2 in map:
        for prereq in map[course2]:
            graph.get(prereq, set()).add(course2)
    res = []

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
 'Advanced Algorithms', 'Operating Systems',
 'Databases',
 ] == precourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }) or ['Intro to Programming',
 'Data Structures',
 'Advanced Algorithms', 'Databases','Operating Systems'
 
 ] == precourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] })

assert precourses(["Course10", "Course0"], {"Course10": ["Course0"]}) == ["Course0", "Course10"]
assert precourses([], {}) == []
assert precourses(["Course1"], {}) == ["Course1"]
assert precourses(
    ["Course1", "Course2", "Course3"],
    {"Course1": ["Course2"], "Course2": ["Course3"], "Course3": ["Course1"]},
) == []
assert precourses(
    ["Course1", "Course2", "Course3"],
    {"Course2": ["Course1"], "Course3": ["Course1", "Course2"]},
) == ["Course1", "Course2", "Course3"]
assert precourses(
    ["Course1", "Course2", "Course3"],
    {"Course2": ["Course1"], "Course3": ["Course2", "Course1"]},
) == ["Course1", "Course2", "Course3"]
assert precourses(
    ["Course1", "Course2", "Course3"],
    {"Course2": ["Course1"], "Course3": ["Course1"], "Course2": ["Course3"]},
) == ["Course1", "Course3", "Course2"]


# took 32 minutes