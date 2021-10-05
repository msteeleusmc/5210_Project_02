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
        self.addEdge(1, 2)
        self.addEdge(1, 3)
        self.addEdge(2, 4)
        self.addEdge(2, 5)
        self.addEdge(3, 6)
        self.addEdge(3, 7)
        self.addEdge(4, 8)
        self.addEdge(4, 9)
        self.addEdge(5, 10)
        self.addEdge(5, 11)
        self.addEdge(6, 12)
        self.addEdge(6, 13)
        self.addEdge(7, 14)
        self.addEdge(7, 15)
        return self

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
        self.addEdge(1, 2)
        self.addEdge(1, 3)
        self.addEdge(2, 4)
        self.addEdge(2, 5)
        self.addEdge(3, 6)
        self.addEdge(3, 7)
        self.addEdge(4, 8)
        self.addEdge(4, 9)
        self.addEdge(5, 10)
        self.addEdge(5, 11)
        self.addEdge(6, 12)
        self.addEdge(6, 13)
        self.addEdge(7, 14)
        self.addEdge(7, 15)
        self.addEdge(8, 16)
        self.addEdge(8, 17)
        self.addEdge(9, 18)
        self.addEdge(9, 19)
        self.addEdge(10, 20)
        self.addEdge(10, 21)
        self.addEdge(11, 22)
        self.addEdge(11, 23)
        self.addEdge(12, 24)
        self.addEdge(12, 25)
        self.addEdge(13, 26)
        self.addEdge(13, 27)
        self.addEdge(14, 28)
        self.addEdge(14, 29)
        self.addEdge(15, 30)
        self.addEdge(15, 31)
        self.addEdge(16, 32)
        self.addEdge(16, 33)
        self.addEdge(17, 34)
        self.addEdge(17, 35)
        self.addEdge(18, 36)
        self.addEdge(18, 37)
        self.addEdge(19, 38)
        self.addEdge(19, 39)
        self.addEdge(20, 40)
        self.addEdge(20, 41)
        self.addEdge(21, 42)
        self.addEdge(21, 43)
        self.addEdge(22, 44)
        self.addEdge(22, 45)
        self.addEdge(23, 46)
        self.addEdge(23, 47)
        self.addEdge(24, 48)
        self.addEdge(24, 49)
        self.addEdge(25, 50)
        self.addEdge(25, 51)
        self.addEdge(26, 52)
        self.addEdge(26, 53)
        self.addEdge(27, 54)
        self.addEdge(27, 55)
        self.addEdge(28, 56)
        self.addEdge(28, 57)
        self.addEdge(29, 58)
        self.addEdge(29, 59)
        self.addEdge(30, 60)
        self.addEdge(30, 61)
        self.addEdge(31, 62)
        self.addEdge(31, 63)

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

    # Make a class object of the warehouse size 15
    warehouse = Warehouse(16)

    # Create the layout of the warehouse
    warehouse.createGraph()

    # Print the warehouse
    #warehouse.printWarehouse(15)
    target = 15
    source = 1
    maxDepth = 4

    if warehouse.IDDFS(source, target, maxDepth) == True:
        print("Warehouse worked: ", True)
    else:
        print("Warehouse worked: ", False)

    shelves = Shelves(64)
    target = 63
    source = 1
    maxDepth = 6

    shelves.createGraph()

    if shelves.shelvesIDDFS(source, target, maxDepth) == True:
        print("Shelfs worked: ", True)
    else:
        print("Shelfs worked: ", False)

    orders = Orders(1)
    order_array = []
    order_size, order_division, order_array = orders.createOrder()

    print("Size of order: ", order_size)
    print("Order division: ", order_division)
    print("Order shelves: ", order_array)