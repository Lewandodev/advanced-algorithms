#Bellman Ford algorithm used on graph problem of "Cheapest flights within K stops"


#Bellman Ford algorithm:
#In graph theory Bellman Ford algorithm is Single source shortest path algorithm which follows dynamic programming strategy meaning
#it will find shortest path form one node to other, we try all possible solutions and pick up the best one
#Bellman Ford algorithm has slower time complexity than other shortest path algorithms (such as Dijkstra) and is used only in specific graph problems

#Bellman Ford algorithm is used when graph has negative edge weights (like our problem) in such cases Dijkstra fails.
#B.F. can detect negative cycles and determine their occurance. Application of Bellman-Ford algorithm can be found in finance and economics
#for exmp.:when performing arbitrage between markets

#Defining variables in Bellman Ford algorithm
# E - number of edges
# V - number of vertices
# S - starting node
# D - an array the size of V that tracks best distance from S to each node

#Steps
#1. set every entry in D to positive inf. we don't know what the distance to other nodes is
#2. set starting node to 0 D[S]=0 it's our starting point
#3. Relax each edge V-1 times (relaxing edge means taking an edge and trying to update the value from where dge starts to where it ends)
#We need to run V-1 times because we run edges in random order so we could run from the vertex that has positive infinity cost
#to another vertex also has positive infinity cost.

#code exmp:
'''for i in range(0,v-1):
    for edge in graph.edges:
    we loop v-1 times and for each edge relax edge
    if (D[edge.from]+edge.cost<D[edge.to]) we look at value where edge starts add edge cost and see if thats better than where we trying to go
        D[edge.to]=D[edge.from]+edge.cost if yes, then we update with the shorter path value

'''

#to check for negative cycle we run second time
'''for i in range(0,v-1):
    for edge in graph.edges:
    we loop v-1 times and for each edge relax edge
    if (D[edge.from]+edge.cost<D[edge.to]) we check for any nodes that update to better value than the current best
        D[edge.to]=-inf if yes, they are part of negative cycle, we mark that node as having cost of negative infinity 

'''



#Problem description:

#There are n cities connected by some number of flights. You have been given an array "flights" where flights[i]=[from(i),to(i),price(i)] indicates
#that there is a flight from city from(i) to city to(i) with cost price(i).
#You are also given three integers "src","dst" and "k" return the ""cheapest"" price from "src" to "dst"with at most "k" stops.
#If there is no such route return value -1.

#to solve this problem we will use Bellman Ford algorithm instead of Dijkstra's algorithm mostly because it has better runtime
#and it can deal with engative weights


#Exapmle with visual representation:
#n=3     flights=[[0,1,100],[1,2,200],[0,2,700]]    src=0   dst=2   k=1


#                        0
#                      /  \
#                  100/    \700
#                    /      \
#                   1---------2
#                       200
#shortest past will be from 0 to 2 but the cost is 700
#much better path would be from 0 through 1 ending with  2 where price is smaller and it fits criteria as there is only 1 city between destinations (k=1)
#the result will be 300


#man idea of the algorithm we will write for this problem will be breadth search from our src(source) node and simultaneously keep track of each node we visited
# or can visit and check what is the minimum price that it takes to reach that node. This will go on till we find the best route to our destination

#during the breadth search we will go through every single edge in graph in order to find the minimum price as go from one node to other
#k determines how many layers of arrays we will have (we woll get k+1 arrays)
#we will need 2 price arrays the main "original" and temporary array
#Values will be first put in temporary array
#once we get fully updated temporary array we will copy it values and put them in the main array repleacing the placeholder values (such as infinities)
#we skip edges we haven't got to for the source node (for exmp.: in visual representation getting from 1 to 2 while placeholder is inf is inf+200 not 200 therefore we skip)
#this solution is much more readable and better to code


#temporary values is always copy of original values while we update values we put them and reassign them in main array and loop it k+1 times
#as loop is running k+1 times


#Problem solution with algorithm

def BellmanFordSoultion(n,flights,src,dst,k):
    prices=[float("inf")]*n #prices array size is the number of nodes we are given
    prices[src]=0 #first source node is 0 cause we are starting here

    for i in range(k+1):#iterating through loop
        temp_price=prices.copy()
        for s,d,p in flights:#going through edges
            if prices[s]==float("inf"):
                continue
            if prices[s]+p<prices[d]: #new minimum price/shortest path found
                temp_price[d]=prices[s]+p #we update array as we find new minimum

        prices=temp_price

    if prices[dst]==float("inf"):
        return -1
    else:
        return prices[dst]
