'''
Practice Question
Given a list of packages and a list of dependencies.
Return the list of packages based on the dependencies. order does not matter.

A, B, C, D
A <- B


Hints
1. Can be created as a graph
2. Watch out for circular references
'''
from collections import deque

def main(packages, dependencies):
    dependency_count = {}

    # Initialize counts to 0
    for package in packages:
        dependency_count[package] = 0

    # Initialize counts
    for parent, deps in dependencies.items():
        dependency_count[parent] += len(deps)
    
    # Set initial queue
    output = []
    queue = deque()
    for p, count in dependency_count.items():
        if count == 0:
            queue.append(p)
    
    # Loop through independent packages
    while queue:
        package = queue.pop()
        output.append(package)
        
        for parent, deps in dependencies.items():
            if package in deps:
                dependency_count[parent] -= 1
                if dependency_count[parent] == 0:
                    queue.append(parent)

    if len(packages) != len(output):
        return -1
    return output

print(main(['A','B','C','D'], {'B': ['A'], 'C': ['A','B'], 'D': ['C']}))
print(main(['A','B'], {'B': ['A'], 'A': ['B']}))
