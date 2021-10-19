TO RUN THIS PROGRAM, DOWNLOAD AND SAVE TO YOUR WORKING DIRECTORY.

TO RUN TYPE "python main.py" WITHOUT THE ""


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

###################################################################
Phase 2 cont'd:
The warehouse tree can now traverse to the selected division, and then remain there for the next customers order.
It will then start from that position and print the path to the newly seelcted division. The shelf class then takes effect,
always starting at shelf number 1. It will then iterate through a loop until all shelves are reached. What needs to happen
now is, I will store the sheld path as one long string until the entire order is completed. Then return to 1.
Next phase, I will create a method to store all of this data to a CSV file so that results may be compared. Image supports
what has been accomplished.
![Screenshot (14)](https://user-images.githubusercontent.com/56514179/136617378-c46b9505-7a1d-4458-ab71-a7f3b5cca83c.png)

###################################################################
Phase 3:
I have added methods to store all crucial data into the csv file. Path cost is also stored for the traversal between divisions
and the shelves. Next, the shortest and longest path will be retrieved from the csv file, and the average too.

###################################################################
Phase 3  Cont'd:
The csv functions and files are done. It creates multiple csvs to end with two sorted csv files. The first csv file "sorted"
is used to find the average, shortest, and longest path in the warehouse/division scores. The second csv "sorted2" is used
for the same purpose except to print out average, shortest and longest for shelves paths. Final result pictured below.

![Screenshot (15)](https://user-images.githubusercontent.com/56514179/137240655-33a1ff95-ab7d-4bdf-a65b-a30990be8fee.png)

###################################################################
Question 5 - Project 02

Attached is a screen shot for the division path form division 1 to 
division 6, and the cost for the traversal. Also, in the screen shot
is the traversal from shelf 1 to 33 and returning to 1 with the count 
including exiting the division.

![Question_05](https://user-images.githubusercontent.com/56514179/137604638-60c3241e-688c-416e-a667-512579a57a04.png)

###################################################################
Final Program Output Screen Shots

![Screenshot (17)](https://user-images.githubusercontent.com/56514179/137604927-1d8fea0e-3354-45a4-b838-2ed27e109dd8.png)

![Screenshot (18)](https://user-images.githubusercontent.com/56514179/137604928-52087ce5-5c06-41b3-97d3-e8579a7a9e30.png)

###################################################################

MADE FINAL CHANGES TO OUTPUT:


![Screenshot (19)](https://user-images.githubusercontent.com/56514179/137832623-c47d3434-67e7-4ad7-9c5f-b84b8ebbbf6c.png)

![Screenshot (20)](https://user-images.githubusercontent.com/56514179/137832635-a44e1e3f-fb6b-49e4-8e9e-37ad1387167a.png)

![Screenshot (21)](https://user-images.githubusercontent.com/56514179/137832647-ee942449-8bb8-4cea-824c-e5a80bbf853d.png)

