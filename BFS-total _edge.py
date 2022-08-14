
from collections import defaultdict

visited = []  # List for visited nodes.
queue = []  # Initialize a queue

def bfs(visited, graph, node, destination):  # function for BFS
    if node==destination:
        return 
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph=defaultdict(list)
n=int(input('Enter a number: '))
for i in range(n):
    x,y=input().split()
    if y not in graph[x]: # not repeat valu
        graph[x].append(y)
    if x not in graph[y]: # not repeat valu
        graph[y].append(x)
# print(graph)
# print(graph['1'])
bfs(visited, graph, '1', '5')