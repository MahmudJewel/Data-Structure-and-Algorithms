# Source
#
# & customized

from collections import defaultdict


def dfs(visited, graph, root, parent_node=-1):  # function for dfs
    visited.add(root)
    for neighbour in graph[root]:
        if neighbour not in visited:
            if dfs(visited, graph, neighbour, root) in visited:
                print('dfs-1')
                return 1
            elif neighbour != root:
                print('Not root-1')
                return 1
        # dfs(visited, graph, neighbour)
    print('Terminated')
    return 0


# making graph according to user input.
graph = defaultdict(list)
n = int(input('Enter the number of connecting roads => '))
for i in range(n):
    x, y = map(int, input().split())
    if y not in graph[x]:  # not repeat valu
        graph[x].append(y)
    if x not in graph[y]:  # not repeat valu
        graph[y].append(x)
root = int(input('Enter the root node: '))
# print('Graph is ==> ', graph)

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

visited = set()  # used as stack
# Driver Code
# print("Following is the Depth-First Search")
cycle = 0
result = dfs(visited, graph, root)
print('Result==> ', result)
if result == 1:
    print('Cycle found')
else:
    print('Cycle not found')
