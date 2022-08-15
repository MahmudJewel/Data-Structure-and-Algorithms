'''
6
1 2
2 3
3 4
4 5
5 6
4 6
'''

from collections import defaultdict
graph=defaultdict(list)
n=int(input('Enter the number of connecting roads => '))
for i in range(n):
    # x,y=map(int, input().split())
    x,y=input().split()
    if y not in graph[x]: # not repeat valu
        graph[x].append(y)
    if x not in graph[y]: # not repeat valu
        graph[y].append(x)
print(graph)
for i in graph:
    print(i, graph[i])
