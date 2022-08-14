
from collections import defaultdict
graph=defaultdict(list)
weight={}   # weights
n=int(input('Enter the number of connecting roads => '))
for i in range(n):
    x,y,w=map(int, input().split())
    # x,y=input().split()
    if y not in graph[x]: # not repeat value
        graph[x].append(y)
        weight[x,y]=w # store weights
    if x not in graph[y]: # not repeat value
        graph[y].append(x)
        weight[y,x]=w # store weights
print('Graphs are => ',graph)
print('Weights are => ',weight) # Weights
print('Weights are => ',weight[1,2]) # Weights
