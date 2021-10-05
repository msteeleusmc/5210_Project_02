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

    def DLS(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.warehouse[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False

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
    def shelvesIDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.shelvesDLS(src, target, i)):
                return True
        return False

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

    def orderSize(self):
        order_size = random.randint(1, 3)
        return order_size

    def getDivision(self):
        order_division = random.randint(1,15)
        return order_division

    def getShelves(self, order_size):
        shelf_array = []
        for i in range(0, order_size):
            shelf_array.append(random.randint(1, 63))

        return shelf_array

    def createOrder(self):
        order_size = self.orderSize()
        order_division = self.getDivision()
        shelf_array = self.getShelves(order_size)

        return order_size, order_division, shelf_array;

#######################################################################
#                          Main function
#######################################################################
if __name__ == '__main__':
    count = 0
    root = 1
    while count in range (0, 100):
        orders = Orders(1)
        order_array = []
        order_size, order_division, order_array = orders.createOrder()

        print("Size of order: ", order_size)
        print("Order division: ", order_division)
        print("Order shelves: ", order_array)

        # Make a class object of the warehouse size 15
        warehouse = Warehouse(16)

        # Create the layout of the warehouse
        warehouse.createGraph()

        source = root
        target = order_division
        maxDepth = 4

        if warehouse.IDDFS(source, target, maxDepth) == True:
            print("Warehouse worked: ", True)
        else:
            print("Warehouse worked: ", False)

        shelves = Shelves(64)

        shelves.createGraph()

        shelf_source = 1
        shelf_target = 0
        shelf_depth = 6

        for i in order_array:
            shelf_target = i

            if shelves.shelvesIDDFS(shelf_source, shelf_target, shelf_depth) == True:
                print("Shelfs worked: ", True)
            else:
                print("Shelfs worked: ", False)


        count += 1