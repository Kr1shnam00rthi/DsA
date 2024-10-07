 n=int(input())
 m=int(input())
 
 # n no of nodes
 # m no of edges
 
 adj_list=[][] # 0 based index
 
 for i in range(m):
 	u=int(input())
 	v=int(input())
 	adj_list[u].append(v)
 	adj_list[v].append(u)

 	# undirected graphs
 	
 	# in directed graphs only one append is required based of direction
 	
