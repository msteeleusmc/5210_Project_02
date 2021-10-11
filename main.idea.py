from collections import defaultdict
import random

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
                print(path)
                return path
            else:
                path = self.alternateDFS(self.warehouse, source, target, path)
                print(path)
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

    def altPrintPath(selfself, path):
        for i in path:
            print(i)

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
                # return True
                # run a while-loop for the queue
                while q:
                    # Dequeue a vertex from q[]
                    dq = q.pop(0)
                    # if dq == target then print the path
                    if dq == target:
                        self.printPath(parent, dq, path)
                        self.returnToSource(path)
                        return path

                    for i in self.shelves[dq]:
                        if visited[i] == False:
                            q.append(i)
                            visited[i] = True
                            parent[i] = dq

    # function will print the path of the shelf traversal from 1 to target
    def printPath(self, source, x, path):
        path_len = 1
        if source[x] == -1 and x < self.V:
            path.append(x)
            #print(x)
            return 0

        temp = self.printPath(source, source[x], path)
        path_len = temp + path_len

        if x < self.V:
            path.append(x)
            #print(x)

        return path_len

    # function will make a path list going from 1 to source back to 1
    def returnToSource(self, path):
        temp = path
        for i in reversed(temp):
            path.append(i)

        for i in range(1,len(path)-1):
            if path[i] == path[i-1]:
                path.remove(path[i])

        return path


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
    warehouse_root = 1
    shelf_root = 1

    # This while-loop runs until 100 customer orders are completed
    while count in range (0, 1):
        # orders creates a customer order instance
        orders = Orders(1)
        # order array will be used to track which shelves are in the division
        order_array = []
        # return values to know the size, division , and shelves for the order
        order_size, order_division, order_array = orders.createOrder()
        order_array.sort()

        # print statement; delete later
        print("Size of order: ", order_size)
        print("Order division: ", order_division)
        print("Order shelves: ", order_array)

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

        print("Warehouse:")
        # run the IDS algorithm to see if the target can be reached
        # from the current source node
        warehousePath = warehouse.IDS(source, target, maxDepth)
        # if length > 0 print path this way
        if warehousePath is None:
            pass
        else:
            if len(warehousePath) > 0:
                ################################################
                # Create a csv object for storing the warehouse
                # path traveled
                ################################################
                warehouse.altPrintPath(warehousePath)

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



########## My ideas begin here ##############
# I added some code to make an actual path that avoids reduncancy
# when robot moves in-between nodes





######### create empty list of paths to populate from shelves class iteration 

        list_of_paths = []
        
        # for-loop will run through each item in the order array to verify that the shelf was found
        for i in order_array:
            shelf_target = i
            
        
            
            print("Shelf:")
            # Using the same IDS algorithm as before
            shelfPath = shelves.shelvesIDS(shelf_source, shelf_target, shelf_depth)
            print(shelfPath)
            
            list_of_paths.append(shelfPath)
            
        
####### These below create an actual path with no redundancy
       
        if len(list_of_paths) == 1:        
        
            #Nothing to do
            path = list_of_paths[0]
            


        if len(list_of_paths) == 2:

            #pop matching numbers from end of a and beggining of b
            a = list_of_paths[0]
            b = list_of_paths[1]
    
            while a[-1] == b[0]:
                last_matching_number = a[-1]
                a.pop(-1)
                b.pop(0)
    
            a.append(last_matching_number)
            path = a + b

    
    
        if len(list_of_paths) == 3:

            #pop matching numbers from end of a and beggining of b, 
            #make a new list and compare it with c to keep popping.
            a = list_of_paths[0]
            b = list_of_paths[1]
            c = list_of_paths[2]

    
            while a[-1] == b[0]:
                last_matching_number = a[-1]
                a.pop(-1)
                b.pop(0)
    
            a.append(last_matching_number)
    
            a = a + b
    
            while a[-1] == c[0]:
                last_matching_number = a[-1]
                a.pop(-1)
                c.pop(0)
    
            a.append(last_matching_number)
    
            path = a + c
    
        
    
        print(f'actual path: {path}')
      
        
####### End of edits by Antonio 



        # re-assign the shelf root as the first node shelf
        shelf_root = 1

        print("\n\n")
        # Increase the count
        count += 1