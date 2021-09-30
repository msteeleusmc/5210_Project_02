# Begin by creating a weighted unidrected graph

# Function will add edges to the graph
def addEdge(warehouse, A, B, weight):

    warehouse[A].append([B, weight])
    warehouse[B].append([A, weight])

    return warehouse

# Function to create the graph
def createGraph(warehouse):
    addEdge(warehouse, 1, 2, 20)
    addEdge(warehouse, 1, 3, 20)
    addEdge(warehouse, 2, 4, 20)
    addEdge(warehouse, 2, 5, 30)
    addEdge(warehouse, 3, 6, 40)
    addEdge(warehouse, 3, 7, 10)
    addEdge(warehouse, 4, 8, 10)
    addEdge(warehouse, 4, 9, 20)
    addEdge(warehouse, 5, 10, 30)
    addEdge(warehouse, 5, 11, 20)
    addEdge(warehouse, 6, 12, 30)
    addEdge(warehouse, 6, 13, 20)
    addEdge(warehouse, 7, 14, 20)
    addEdge(warehouse, 7, 15, 20)

    return warehouse


# Print the graph as an adjacency list
def printWarehouse(warehouse, V):

    for i in range(1, V):
        print(i, " shares edge with ")

        for j in warehouse[i]:
            A = j[0]
            weight = j[1]

            print("\t", A, " and edge has weight of ", weight)

if __name__ == '__main__':

    shelves = 16

    warehouse = [[] for i in range(shelves)]

    # Create the graph
    createGraph(warehouse)

    # Print graph
    printWarehouse(warehouse, 16)