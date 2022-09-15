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

