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

