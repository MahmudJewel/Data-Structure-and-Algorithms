# Source 
# https://favtutor.com/blogs/depth-first-search-python
# & customized

from collections import defaultdict

def dfs(visited, graph, root):  # function for dfs 
		if root not in visited:
			print (root)
			visited.add(root)
			# print('visited: ', visited)
			for neighbour in graph[root]:
				dfs(visited, graph, neighbour)

# making graph according to user input. 
graph=defaultdict(list)
n=int(input('Enter the number of connecting roads => '))
for i in range(n):
		x,y=map(int, input().split())
		# x,y=input().split()
		# graph[x].append(y)
		# graph[y].append(x)
		if y not in graph[x]: # not repeat valu
			graph[x].append(y)
		if x not in graph[y]: # not repeat valu
			graph[y].append(x)
root=int(input('Enter the root node: '))
print('Graph is ==> ',graph)

'''
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
6
5 3
5 7
3 2
3 4
7 8
4 8
'''

visited = set()  # used as stack
# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, root)
