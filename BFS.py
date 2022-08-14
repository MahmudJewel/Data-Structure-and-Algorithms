# Source
# https://favtutor.com/blogs/breadth-first-search-python
# & customized

from collections import defaultdict

# graph = {
#     '5': ['3', '7'],
#     '3': ['2', '4'],
#     '7': ['8'],
#     '2': [],
#     '4': ['8'],
#     '8': []
# }

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, root):  # function for BFS
    visited.append(root)
    queue.append(root)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
# making graph according to user input. 
graph=defaultdict(list)
n=int(input('Enter the number of connecting roads => '))
for i in range(n):
        # x,y=map(int, input().split())
        x,y=input().split()
        # graph[x].append(y)
        # graph[y].append(x)
        if y not in graph[x]: # not repeat value
            graph[x].append(y)
        if x not in graph[y]: # not repeat value
            graph[y].append(x)
print('Graph is ==> ',graph)
print("Following is the Breadth-First Search")
root=input('Enter the root: ')
bfs(visited, graph, root)    # function calling
