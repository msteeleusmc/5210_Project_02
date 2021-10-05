# 5210_Project_02
Iterative Deeping Search (IDS)

This is project 2 for CSCE 5210

Phase 1: 
I created an undirected weighted graph to establish my environment. I used 15 nodes, and 
added the predetermined weights to their edges based on project 2 documentation. Inspiration for
making this graph came from https://www.geeksforgeeks.org/graph-implementation-using-stl-for-competitive-programming-set-2-weighted-graph/

![Screenshot (13)](https://user-images.githubusercontent.com/56514179/135544796-06c6b126-7fba-4270-a7d7-ec216463e6d5.png)

![Screenshot (12)](https://user-images.githubusercontent.com/56514179/135544822-b89870de-88bd-442f-bfe0-3e3e88a34f0b.png)

####################################################################
Phase 1 cont'd: 
I decided to make a class versus just using function calls as done in Project 1. This of course
takes an object oriented approach to control which data structures accesses data. By creating a 
warehouse class, I would only be able to call those specific functions if intended too.

####################################################################
Phase 2:
Created an IDS and DFS algorithm for the warehouse class to confirm a path existed between the 
source node and the target node. After this was successful with the warehouse class, a shelves 
class was then created to create a tree within the division for 63 shelves. This class also uses
an IDS algorithm to search from node 1 to whichever shlef is the target node. The final thing done
during this time, was creating an orders class to create a customers order per the requirements
outlined in the project 2 description. When called, the class will generate an order size, then 
a random division number, then random shleves not to exceed the size of the customers order. The
customers order shall not be greater than size of 3.
