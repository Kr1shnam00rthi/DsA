# n= no of nodes
# m= no of edges

n,m=int(input())
adj=[[0 for i in range(n+1)] for j in range(n+1)] # 0 indexed graphs

# for undirected graphs
for i in range(m):
	u=int(input())
	v=int(input())
	adj[u][v]=1 
	adj[v][u]=1

# This method take n^2 space
