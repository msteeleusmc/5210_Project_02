from collections import defaultdict

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
        print(True)
    else:
        print(False)