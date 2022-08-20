# Title: Cycle detection using DFS
# Source: own
# Theory: https://www.youtube.com/watch?v=Pg9ZXkQgRaE

# Theory: If visited node is not parent node, then Cycle is existed

from collections import defaultdict
def dfs(graph, visited, root, parent_node=-1):  # function for dfs
    # print('Parent+> ', parent_node)
    visited.add(root) # make root nod visited
    for neighbour in graph[root]: # adjacent node
        if neighbour not in visited: # if adj not visited, run dfs
            if dfs(graph, visited, neighbour, root): # if adj return true, cycle found
                print('dfs-1')
                return True
        else:
            if neighbour != parent_node: # if visited and adj & parent node are same, cycle found
                print('Not root-1')
                return True
    # print('Terminated')
    return False # if above condition false, Cycle not found


'''
7
1 2
1 3
2 4
2 5
3 6
3 7
4 5    cycle
'''

# making graph according to user input.
graph = defaultdict(list)
n = int(input('Enter the number of connecting roads => '))
for i in range(n):
    x, y = map(int, input().split())
    if y not in graph[x]:  # not repeat value
        graph[x].append(y)
    if x not in graph[y]:  # not repeat value
        graph[y].append(x)
root = int(input('Enter the root node: '))
print('Graph is ==> ', graph)


visited = set()  # used as stack
# Driver Code
cycle = 0
result = dfs(graph, visited, root)
print('Result==> ', result)
if result:
    print('Cycle found')
else:
    print('Cycle not found')
