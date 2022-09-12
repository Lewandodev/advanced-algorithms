#Bellman Ford algorithm used on graph problem of "Cheapest flights within K stops"


#Bellman Ford algorithm:
#Single source shortest path algorithm used in graph problems which follows dynamic programming strategy.: we try all possible solutions and pick up the best one


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

#during the breadth search we will go through every single edge in graph in order to find the minimum path as prices will consist of 2 arrays
#

