# this is leet code problem solution (207) Course Schedule

from collections import defaultdict

def canFinish(numCourses, prerequisites):
    # Create a graph using an adjacency list
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # Populate the graph and in-degrees
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue with courses that have no prerequisites
    queue = []
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    # Perform a topological sort
    while queue:
        course = queue.pop(0)
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # If all courses have been taken (in-degree reduced to 0), it's possible
    return sum(in_degree) == 0

# Example usage:
numCourses = 2
prerequisites = [[1, 0]]
result = canFinish(numCourses, prerequisites)
print(result)  # This should print True
