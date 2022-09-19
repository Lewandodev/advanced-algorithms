#dijkstra algorithm is dynamic programming algorithm used in shortest path graph problems

#quick reminder about graphs
#each pair of two different nodes with some weight is called edge, path is definied as sequence of nodes
#length of each path is sum of weights of the edges corresponding to path

#To solve the problem of finding the shortest path for each node when weights of edges are non-negative we use Djisktra algorithm



#Dijkstra Alg. principle:
#To find the shortest path from source to a node it is enough to consider only adjacent nodes of that node

#Dijkstra Algorithm in steps:
###what we will need:###
# s- source node
# w- distance between nodes u and v
# w(uv)>=0, d(v)- path length from s to v
#Pemranent nodes: shortest paths lengths
#Temporary nodes: upper bounds on the shortest path lengths

#Steps:
#1) -mark all nodes as temporary
#2) -assign d(v) to infinity for v!=s and d(s) to 0
#3) -choose temporary node u with the smallest path length
#4) - mark u as permanent
#5) - d(v)=min{d(v),d(u)+w(uv)} for every temporary node v to adjacent to u (we use recursion here)
#6)- if no temporary nodes left Stop, other wise go to step 2



#Dijkstra algorithm in code:
#regardless of implementation we will use dictionaries
graph={}

#simpler version
#we use graph that is initally defined
def dijkstra_s(graph,start,goal):
    shortest_distance={} #will be updated
    prior={} #used to find shortest path
    inv_nodes=graph #nodes we wont see we will be running through them until the are all seen















#shorter version more advanced version
#graph will be implemented later in the function
def dijkstra_a(nodes,edges,source_index=0):
    path_lenghts={v: float('inf') for v in nodes} #Initially each path length is assigned to infinity expect source node
    path_lenghts[source_index]=0

    #then we set the edges dictionary where keys are node pairs and values are distances
    adjacent_nodes={v: {} for v in nodes}
    for (u,v),w_uv in edges.items():
        adjacent_nodes[u][v]=w_uv
        adjacent_nodes[v][u]=w_uv

    temporary_nodes=[v for v in nodes] #contains all the nodes
    while len(temporary_nodes)>0: #we iterate till there is no temporary node left
        upper_bounds={v:path_lenghts[v] for v in temporary_nodes}
        u=min(upper_bounds,key=upper_bounds.get())
        #we first find the temporary node with smallest path length called "u" then remove it
        temporary_nodes.remove(u)

        #lastly we update path length for every temporary adjacent node to "u"
        #we use recursion here
        for v,w_uv in adjacent_nodes[u].items():
            path_lenghts[v]=min(path_lenghts[v],path_lenghts[u]+w_uv)

        return path_lenghts


