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
    def addEdge(self, A, B, weight):
        self.warehouse[A].append([B, weight])
        self.warehouse[B].append([A, weight])
        return self.warehouse

    # Function called to create the graph
    def createGraph(self):
        self.addEdge(1, 2, 20)
        self.addEdge(1, 3, 20)
        self.addEdge(2, 4, 20)
        self.addEdge(2, 5, 30)
        self.addEdge(3, 6, 40)
        self.addEdge(3, 7, 10)
        self.addEdge(4, 8, 10)
        self.addEdge(4, 9, 20)
        self.addEdge(5, 10, 30)
        self.addEdge(5, 11, 20)
        self.addEdge(6, 12, 30)
        self.addEdge(6, 13, 20)
        self.addEdge(7, 14, 20)
        self.addEdge(7, 15, 20)
        return self

    # Print the warehouse
    def printWarehouse(self, V):
        for i in range(1, V+1):
            print(i, " shares edge with:")

            for j in self.warehouse[i]:
                A = j[0]
                weight = j[1]
                print("\t", A, " and edge weight is: ", weight)


#######################################################################
#                          Main function
#######################################################################
if __name__ == '__main__':

    # Make a class object of the warehouse size 15
    warehouse = Warehouse(15)

    # Create the layout of the warehouse
    warehouse.createGraph()

    # Print the warehouse
    warehouse.printWarehouse(15)