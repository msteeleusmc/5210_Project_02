from collections import defaultdict
import random
import csv
import os
import pandas as pd

class Warehouse:

    # Constructor function
    def __init__(self, nodes):
        # Define the number of divisions 1 - 15
        self.divisions = nodes
        # default dictionary to store graph/tree of warehouse
        self.warehouse = defaultdict(list)
        self.cost = 0

    # Function will add edges to the graph and their weights
    def addEdge(self, A, B):
        self.warehouse[A].append(B)
        self.warehouse[B].append(A)
        return self.warehouse

    # Function called to create the graph
    def createGraph(self):
        count = 1
        j = 1
        # for-loop creates the tree and edges
        for i in range(2, 16):
            if count == 1:
                self.addEdge(j, i)
                count += 1
            elif count == 3:
                j += 1
                self.addEdge(j, i)
                count = 2
            else:
                self.addEdge(j, i)
                count += 1

    # This funciton called to find the target from the source
    def DLS(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.warehouse[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    # IDS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDS(self, source, target, maxDepth):

        # used to store the path traveled
        visited = [False] * (self.divisions)
        parent = [-1] * (self.divisions)
        path = []

        # create a queue for search
        q = []

        # source node is appended first
        q.append(source)
        # mark the source as a visited node
        visited[source] = True

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(source, target, i)):
                path = self.alternateDFS(self.warehouse, source, target, path)
                #print(path)
                return path
            else:
                path = self.alternateDFS(self.warehouse, source, target, path)
                #print(path)
                return path


    def alternateDFS(self, warehouse, source, target, path=[]):
        path = path + [source]

        if source == target:
            return path

        for node in self.warehouse[source]:
            if node not in path:
                newpath = self.alternateDFS(warehouse, node, target, path)
                if newpath:
                    return newpath

    def getCost(self, pathWeights, w_cost):
        # For loop will check the pathWeights and create a summation for total cost
        for i in pathWeights:
            if i == [1, 2] or i == [2, 1]:
                w_cost += 20
            if i == [1, 3] or i == [3, 1]:
                w_cost += 20
            if i == [2, 4] or i == [4, 2]:
                w_cost += 20
            if i == [2, 5] or i == [5, 2]:
                w_cost += 30
            if i == [3, 6] or i == [6, 3]:
                w_cost += 40
            if i == [3, 7] or i == [7, 3]:
                w_cost += 10
            if i == [4, 8] or i == [8, 4]:
                w_cost += 10
            if i == [4, 9] or i == [9, 4]:
                w_cost += 20
            if i == [5, 10] or i == [10, 5]:
                w_cost += 30
            if i == [5, 11] or i == [11, 5]:
                w_cost += 20
            if i == [6, 12] or i == [12, 6]:
                w_cost += 30
            if i == [6, 13] or i == [13, 6]:
                w_cost += 20
            if i == [7, 14] or i == [14, 7]:
                w_cost += 20
            if i == [7, 15] or i == [15, 7]:
                w_cost += 20

        return w_cost

#######################################################################
#                           Shelf Class
#######################################################################
class Shelves:
    # Constructor function
    def __init__(self, nodes):
        # Define the number of divisions 1 - 15
        self.V = nodes
        # default dictionary to store graph/tree of warehouse
        self.shelves = defaultdict(list)

    # Function will add edges to the graph and their weights
    def addEdge(self, A, B):
        self.shelves[A].append(B)
        self.shelves[B].append(A)
        return self.shelves

    # Function called to create the graph
    def createGraph(self):
        count = 1
        j = 1
        # for-loop creates the tree and its edges
        for i in range(2, 64):
            if count == 1:
                self.addEdge(j, i)
                count += 1
            elif count == 3:
               j += 1
               self.addEdge(j, i)
               count = 2
            else:
                self.addEdge(j, i)
                count += 1

    # Called to fund the target from the source
    def shelvesDLS(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.shelves[src]:
            if (self.shelvesDLS(i, target, maxDepth - 1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def shelvesIDS(self, source, target, maxDepth):

        # used to store the path traveled
        visited = [False] * (self.V)
        parent = [-1] * (self.V)
        path = []

        # create a queue for search
        q = []

        # source node is appended first
        q.append(source)
        # mark the source as a visited node
        visited[source] = True

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.shelvesDLS(source, target, i)):
                path = self.alternateDFS(self.shelves, source, target, path)
                return path
            else:
                path = self.alternateDFS(self.shelves, source, target, path)
                return path

    def alternateDFS(self, shelves, source, target, path=[]):
        path = path + [source]

        if source == target:
            return path

        for node in self.shelves[source]:
            if node not in path:
                newpath = self.alternateDFS(shelves, node, target, path)
                if newpath:
                    return newpath

#######################################################################
#                      Customer Order Class
#######################################################################
class Orders:
    # Constructor function
    def __init__(self, nodes):
        # Define the number of divisions 1 - 15
        self.V = nodes
        # default dictionary to store graph/tree of warehouse
        self.orders = defaultdict(list)

    # This function will return the random order size
    def orderSize(self):
        order_size = random.randint(1, 3)
        return order_size

    # This function will return a random division number
    def getDivision(self):
        order_division = random.randint(1,15)
        return order_division

    # This function will generate a random array of shelf numbers
    # equal to the size of the order
    def getShelves(self, order_size):
        shelf_array = []
        for i in range(0, order_size):
            shelf_array.append(random.randint(1, 63))

        return shelf_array

    # This function calls all others to create a customer order
    # Returns to the main function
    def createOrder(self):
        order_size = self.orderSize()
        order_division = self.getDivision()
        shelf_array = self.getShelves(order_size)

        return order_size, order_division, shelf_array;

#######################################################################
#                      Global CSV Functions
#######################################################################
def findAverage():
    pass

def findLongestPath():
    pass

def findShortestPath():
    pass


#######################################################################
#                          Main function
#######################################################################
if __name__ == '__main__':
    # count helps track the number of customer orders.
    count = 0
    # root is the starting node. It will update as the robot
    # transistions the warehouse with a new starting node
    warehouse_root = 1
    shelf_root = 1

    # This while-loop runs until 100 customer orders are completed
    while count in range (0, 100):
        # orders creates a customer order instance
        orders = Orders(1)
        # return values to know the size, division , and shelves for the order
        order_size, order_division, order_array = orders.createOrder()
        order_array.sort()

        # Make a class object of the warehouse size 15
        warehouse = Warehouse(16)

        # Create the layout of the warehouse
        warehouse.createGraph()

        # source node is the current root (position) of the robot
        source = warehouse_root
        # target is the destination node (division) for the order
        target = order_division
        # max depth of the division tree is 4
        maxDepth = 4

        # run the IDS algorithm to see if the target can be reached
        # from the current source node
        warehousePath = warehouse.IDS(source, target, maxDepth)

        # assign the new root node as the current position
        warehouse_root = order_division

        # create a shelves object
        shelves = Shelves(64)
        # create a shelf layout for the current division
        shelves.createGraph()

        # the shelf root always begins at 1 and updates based on filling the array
        shelf_source = shelf_root
        # the target will be an item in the order array
        shelf_target = 0
        # the depth will be 6 for 63 nodes
        shelf_depth = 6

        endShelves = False
        newPath = []
        # for-loop will run through each item in the order array to verify that the shelf was found
        for i in order_array:
            shelf_target = i
            # Using the same IDS algorithm as before
            shelfPath = shelves.shelvesIDS(shelf_source, shelf_target, shelf_depth)
            shelf_source = shelf_target
            newPath = newPath + shelfPath

        shelfPath = shelves.shelvesIDS(shelf_source, shelf_root, shelf_depth)
        newPath = newPath + shelfPath

        temp = len(newPath) - 1
        while temp > 0:
            if newPath[temp] == newPath[temp - 1]:
                newPath.remove(newPath[temp])
                temp = len(newPath) - 1
            else:
                temp -= 1

        # Create a copy of the current warehouse path
        tempWareHousePath = warehousePath.copy()

        # Create a list object to store a list of weights
        pathWeights = []
        w_cost = 0

        # While-loop will iterate through the new list creating tuples
        while len(tempWareHousePath) > 1:
            pathWeights.append([tempWareHousePath[0], tempWareHousePath[1]])
            tempWareHousePath.pop(0)

        # Call function to return the total path cost for the divisions
        w_cost = warehouse.getCost(pathWeights, w_cost)

        # Create data structures for the csv file
        header = ['Order Size', 'Order Division', 'Current Position', 'Shelves', 'Warehouse Path', 'Warehouse Path Cost', 'Shelf Path', 'Shelf Path Cost']
        data = [order_size, order_division, warehousePath[0], order_array, warehousePath, w_cost, newPath, len(newPath)]
        csv_path = "customer_order.csv"

        # Write to the csv file
        if os.path.exists(csv_path):
            with open('customer_order.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
                f.close()
        else:
            with open('customer_order.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)
                f.close()

        # re-assign the shelf root as the first node shelf
        shelf_root = 1

        # Increase the count
        count += 1

    # Copy csv to another for the following
    df = pd.read_csv('customer_order.csv')
    df.to_csv('copy_' + 'customer_order.csv')

    # Read the data from the new csv and then sort
    df = pd.read_csv('copy_customer_order.csv')
    sorted_df = df.sort_values(by=['Warehouse Path Cost'], ascending=True)
    sorted_df.to_csv('sorted.csv', index=False)

    # Find the average warehouse path from the csv
    path_data = pd.read_csv('sorted.csv')
    # Find the number of rows in the csv
    num_rows = len(path_data.index)
    # Divide by 2 then subtract 1
    num_rows = num_rows / 2
    num_rows -= 1
    # Convert back to int
    num_rows = int(num_rows)
    # Find the average path in the sorted csv with the converted int as the index
    warehouse_avg = path_data['Warehouse Path'].iloc[num_rows]

    print("Warehouse Average Path:\n")
    print(warehouse_avg)
    print()

    # Find the shortest warehouse path from the csv
    shortest_path = path_data['Warehouse Path'].iloc[0]

    print("Warehouse Shortest Path:\n")
    print(shortest_path)
    print()

    # Find longest warehouse path from the csv
    longest_path = path_data['Warehouse Path'].iloc[-1]

    print("Warehouse Longest Path:\n")
    print(longest_path)
    print()

    # Re-sort the csv for shelf path
    df = pd.read_csv('sorted.csv')
    sorted_df = df.sort_values(by=['Shelf Path Cost'], ascending=True)
    sorted_df.to_csv('sorted2.csv', index=False)

    # Find the average shelf path from the csv
    path_data = pd.read_csv('sorted2.csv')
    # Find the number of rows in the csv
    num_rows = len(path_data.index)
    # Divide by 2 then subtract 1
    num_rows = num_rows / 2
    num_rows -= 1
    # Convert back to int
    num_rows = int(num_rows)
    # Find the average path in the sorted csv with the converted int as the index
    shelf_avg = path_data['Shelf Path'].iloc[num_rows]

    print("Shelf Average Path:\n")
    print(shelf_avg)
    print()

    # Find the shortest shelf path from the csv
    shortest_path = path_data['Shelf Path'].iloc[0]

    print("Shelf Shortest Path:\n")
    print(shortest_path)
    print()

    # Find the longest shelf path from the csv
    longest_path = path_data['Shelf Path'].iloc[-1]

    print("Shelf Longest Path:\n")
    print(longest_path)
    print()
