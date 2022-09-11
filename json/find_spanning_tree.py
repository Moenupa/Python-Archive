def prim_find_min_spanning_tree(G):
	'''
	calcuate a minimum spanning tree in Python
	using Prim's algorithm
	ASSUME the input is always valid (in matrix form)
	'''
	n, n_visited = len(G), 1                                # number of nodes / visited nodes
	V_visited = [ 0 for i in range(n) ]                     # V_visited: visited nodes in G
	V_visited[0] = 1                                        # start with the first
	print("src-des : weight ")
	while (n_visited < n):
		src, des = 0, 0
		min = float('inf')
		for i in range(n):
			if V_visited[i]:                                    # node i visited
				for j in range(n):
					if ((not V_visited[j]) and G[i][j] > 0):        # node j not visited and path (i, j) exists\
						if (G[i][j] < min):                           # find minimum path and record
							min = G[i][j] 
							src, des = i, j
		print( "%3d-%-3d :%3d" % (src+1, des+1, G[src][des]) )     # python index 0+, picture index 1+
		V_visited[des] = 1
		n_visited += 1

if __name__ == "__main__":
	G = [
	#   [1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C],
		[0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0], 
		[5, 0, 2, 0, 4, 0, 7, 0, 0, 0, 0, 0], 
		[0, 2, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0], 
		[0, 0, 4, 0, 0, 0, 3, 6, 0, 0, 0, 0], 
		[5, 4, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 0, 3, 0, 2, 0, 0, 1, 0, 0], 
		[0, 7, 1, 3, 0, 2, 0, 8, 0, 9, 1, 0], 
		[0, 0, 0, 6, 0, 0, 8, 0, 0, 0, 1, 4], 
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0], 
		[0, 0, 0, 0, 0, 1, 9, 0, 5, 0, 2, 0], 
		[0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 8], 
		[0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 8, 0], 
	]
	prim_find_min_spanning_tree(G)