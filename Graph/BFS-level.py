from collections import defaultdict

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, root, edge):  # function for BFS
    visited.append(root)
    queue.append(root)
    level=[None]*(edge+1)  # all nodes must be upto edge(0-edge)
    level[root]=0

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                level[neighbour]=level[m]+1
    print('\nLevels are: ',level)
    print("Nodes", " ", "Level")
    for i in range(edge+1):
        print(" ", i,  " --> ", level[i])



# Driver Code
# making graph according to user input. 
graph=defaultdict(list)
edge=int(input('Enter the number of connected nodes => '))
root=int(input('Enter the root node: '))
print('Enter the connected nodes: ')
for i in range(edge):
        # x,y=map(int, input().split())
        x,y=map(int, input().split())
        if y not in graph[x]: # not repeat valu
            graph[x].append(y)
        if x not in graph[y]: # not repeat valu
            graph[y].append(x)

print('Graph is ==> ',graph)
print("Following is the Breadth-First Search: ")
bfs(visited, graph, root, edge)    # function calling