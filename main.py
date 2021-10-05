from collections import defaultdict
import random

#######################################################################
#                           Warehouse Class
#######################################################################
class Warehouse:

    # Constructor function
    def __init__(self, nodes):
        # Define the number of divisions 1 - 15
        self.divisions = nodes
        # default dictionary to store graph/tree of warehouse
        self.warehouse = defaultdict(list)

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
    def IDS(self, src, target, maxDepth):

        # used to store the path traveled
        visited = [False] * (self.divisions)
        parent = [-1] * (self.divisions)

        # create a queue for search
        q = []

        # source node is appended first
        q.append(source)
        # mark the source as a visited node
        visited[source] = True

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                # return True
                # run a while-loop for the queue
                while q:
                    # Dequeue a vertex from q[]
                    dq = q.pop(0)

                    # if dq == target then print the path
                    if dq == target:
                        return self.printPath(parent, dq)

                    for i in self.warehouse[dq]:
                        if visited[i] == False:
                            q.append(i)
                            visited[i] = True
                            parent[i] = dq

    def printPath(self, source, x):
        path_len = 1
        if source[x] == -1 and x < self.divisions:
            print(x)
            return 0

        temp = self.printPath(source, source[x])

        path_len = temp + path_len

        if x < self.divisions:
            print(x)

        return path_len

    # Print the warehouse
    #def printWarehouse(self, V):
    #    for i in range(1, V+1):
    #        print(i, " shares edge with:")

            #for j in self.warehouse[i]:
             #   A = j[0]
              #  weight = j[1]
               # print("\t", A, " and edge weight is: ", weight)

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
    def shelvesIDS(self, src, target, maxDepth):

        # used to store the path traveled
        visited = [False] * (self.V)
        parent = [-1] * (self.V)

        # create a queue for search
        q = []

        # source node is appended first
        q.append(source)
        # mark the source as a visited node
        visited[source] = True

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.shelvesDLS(src, target, i)):
                # return True
                # run a while-loop for the queue
                while q:
                    # Dequeue a vertex from q[]
                    dq = q.pop(0)

                    # if dq == target then print the path
                    if dq == target:
                        return self.printPath(parent, dq)

                    for i in self.shelves[dq]:
                        if visited[i] == False:
                            q.append(i)
                            visited[i] = True
                            parent[i] = dq

    def printPath(self, source, x):
        path_len = 1
        if source[x] == -1 and x < self.V:
            print(x)
            return 0

        temp = self.printPath(source, source[x])

        path_len = temp + path_len

        if x < self.V:
            print(x)

        return path_len

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
#                          Main function
#######################################################################
if __name__ == '__main__':
    # count helps track the number of customer orders.
    count = 0
    # root is the starting node. It will update as the robot
    # transistions the warehouse with a new starting node
    root = 1

    # This while-loop runs until 100 customer orders are completed
    while count in range (0, 10):
        # orders creates a customer order instance
        orders = Orders(1)
        # order array will be used to track which shelves are in the division
        order_array = []
        # return values to know the size, division , and shelves for the order
        order_size, order_division, order_array = orders.createOrder()

        # print statement; delete later
        # print("Size of order: ", order_size)
        # print("Order division: ", order_division)
        # print("Order shelves: ", order_array)

        # Make a class object of the warehouse size 15
        warehouse = Warehouse(16)

        # Create the layout of the warehouse
        warehouse.createGraph()

        # source node is the current root (position) of the robot
        source = root
        # target is the destination node (division) for the order
        target = order_division
        # max depth of the division tree is 4
        maxDepth = 4

        # run the IDS algorithm to see if the target can be reached
        # from the current source node
        if warehouse.IDS(source, target, maxDepth) == True:
            pass#print("Warehouse worked: ", True)
        else:
            pass#print("Warehouse worked: ", False)

        print("\n")

        # create a shelves object
        shelves = Shelves(64)
        # create a shelf layout for the current division
        shelves.createGraph()

        # the shelf root always begins at 1 and updates based on filling the array
        shelf_source = 1
        # the target will be an item in the order array
        shelf_target = 0
        # the depth will be 6 for 63 nodes
        shelf_depth = 6

        # for-loop will run through each item in the order array to verify that the shelf was found
        print("Shelfs:\n")
        for i in order_array:
            shelf_target = i

            # Using the same IDS algorithm as before
            if shelves.shelvesIDS(shelf_source, shelf_target, shelf_depth) == True:
                pass#print("Shelfs worked: ", True)
            else:
                pass#print("Shelfs worked: ", False)

        # Increase the count after each order is completed
        count += 1
        print("\n")