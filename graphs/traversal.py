adj_list1=[[],[2,6],[1,3,4],[],[5],[4,7],[1,7,8],[6,8],[6]]
adj_list2=[[],[2,3],[1,5,6],[1,4,7],[3,8],[2],[2],[3,8],[4,7]]

def bfs(node):
    visited=set()
    queue=[node]
    while len(queue) != 0:
        l = len(queue)
        for _ in range(l):
            n = queue.pop(0)
            if n not in visited:  # Make sure to check if the node has been visited
                visited.add(n)
                print(n, end=" ")
                for x in adj_list1[n]:
                    if x not in visited:
                        queue.append(x)
        print("")


def dfs(node, visited):
    visited.add(node)
    print(node)
    for x in adj_list2[node]:
        if x not in visited:
            dfs(x, visited)


# Test the functions
print("BFS Traversal:")
bfs(1)  # BFS using adj_list1

print("\nDFS Traversal:")
visited = set()
dfs(1, visited)  # DFS using adj_list2

