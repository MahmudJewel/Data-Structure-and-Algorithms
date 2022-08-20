""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from collections import defaultdict
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 20-08-2022 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Source: own
# Theory: Initially all nodes are unvisited
# & customized

# DFS for components
def dfs(visited, graph, root, path):
    if root not in visited:
        path.append(root) # path for connected components
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour, path)
    return path # return each connected components

# making graph according to user input.
graph = defaultdict(list)
edge = int(input('Enter the number of edges => '))
up_node = int(input('Enter the highest number(0-n) => '))
for i in range(edge):
    x, y = map(int, input().split())
    if y not in graph[x]:  # not repeat valu
        graph[x].append(y)
    if x not in graph[y]:  # not repeat valu
        graph[y].append(x)
# root = int(input('Enter the root node: '))
print('Graph is ==> ', graph)

'''
edge= 3
highest node=4
0 1
1 2
3 4 
'''

visited = set()  # used as stack
# connected components
component_count=0
for i in range(up_node):
    if i not in visited:
        path=[]
        pt=dfs(visited, graph,i, path)
        component_count=component_count+1
        print(f"Connected components=> {pt}")
print(f"Total component => {component_count}")

