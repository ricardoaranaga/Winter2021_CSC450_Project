import csv
import sys


def import_file():
    global column_names
    global all_distances
    with open(sys.argv[-1], mode='r') as file:  # To read filename  from command
        csvReader = csv.reader(file, delimiter=',')
        csv_to_dict = csv.DictReader(file)
        dict_obj = csv_to_dict.fieldnames  # Get node names from csv
        column_names = dict_obj[1:]  # Eliminate null value from [0][0] in csv
        # print("Column Names: ",column_names)

        index = 0
        estimators = {}
        for row in csvReader:
            estimators[column_names[index]] = []
            estDict = {}
            for i in range(1, len(row)):
                estDict[column_names[i - 1]] = int(row[i])
            # print(estDict)
            estimators[column_names[index]] = estDict  # Dictionary of nodes w.r.t source and destination
            index += 1
            # print(row)
        # All distances
        all_distances = estimators
        # print(all_distances)

def dijkstra():
    # globals
    DEBUG = False
    topology = []
    nodesDict = {}

    # parsing the command line
    if len(sys.argv) < 2:
        print("Usage: python3 routing.py <topology.csv>")
        exit(0)
    fileName = sys.argv[1]

    # reading the csv file
    with open(fileName, newline='') as file:
        cvsReader = csv.reader(file, delimiter=',')
        for row in cvsReader:
            if DEBUG: print(row)
            topology.append(row)

    # setting node dictionary
    for i in range(1,len(topology[0])):
        nodesDict[topology[0][i]] = i
    if DEBUG: print(nodesDict)

    source = input("Please, provide the source node: ")
    if DEBUG: 
        print('-'*66)
        print("Text entered:{} / source node:{} / value:{}".format(source,source,nodesDict[source])) 
        print('-'*66)

    D = {}
    N = []
    SP = {} 
    # initializing step
    N.append(source) # => add the source to N'
    for n in range(1,len(nodesDict)+1):
        cost = topology[nodesDict[source]][n] 
        w = topology[nodesDict[source]][0]
        v = topology[0][n] # => add the links
        D[v] = cost # => set initial cost
        SP[v] = source # => source as the first step in the SP (Shortest Path) of each path
        if DEBUG: print("cost {} from {} to {}".format(cost,w,v))

    if DEBUG:
        print(('-'*30)+'STEP 0'+('-'*30))
        print(N)
        print(D)
        print('-'*66)

    # Repeating step
    counter = 1
    while(counter < len(D)):
        if DEBUG:
            print('-'*30, end='') 
            print('STEP {}'.format(counter), end='')
            print('-'*30)
        
        temp_D = {key:val for key, val in D.items() if key not in N} # => build a temporary D without nodes in N'
        if len(temp_D) > 0:
            temp = min(temp_D, key=temp_D.get) # => minimum cost between the items in temp D
            if DEBUG: print("Minimum={}, with={}".format(temp,D[temp]))
        
        N.append(temp) # => add the temp to N'
        if DEBUG: print(N)

        for n in range(1,len(D)+1):
            cost = topology[nodesDict[temp]][n] # => get next cost
            w = topology[nodesDict[temp]][0] # => get next node
            v = topology[0][n] # => get previous node
            previous = int(D[v]) # => previous cost in int for calculations
            new = int(D[w])+int(cost) # => get new cost 
            D[v] = min(previous,new) # => compare costs, choose minimum, and set as new cost
            if DEBUG: 
                print("from {} to {} cost {}".format(w,v,cost))
                print("previous v={} with cost={}".format(v,previous)) 
                print("updated v={} with cost={}".format(v,new))
            
            if new < previous: # => if the new cost is less than the previous
                SP[v] = SP[w] + w  # => add to shortest path dictionary
                if DEBUG: print("CHANGED({}) {}".format(v,SP[v]))

        counter += 1

    # building the shortest path string in the required output format
    del SP[source]
    shortestPath = ""
    for node in SP:
        shortestPath += SP[node]+node+', '
    shortestPath = shortestPath[:-2]

    # print resulting outputs
    print("Shortest path tree for node {}:".format(source))
    print(shortestPath)
    print("Costs of the least-cost paths for node {}:".format(source))
    print(str(D).replace('{','').replace('}','').replace("'","")+"\n")


class Network:
    def __init__(self, nodes_count):

        self.nodes = nodes_count  # Total number of nodes in the network_topology
        self.network_topology = []  # Array of nodes


    def nodesdistance(self, s, d, w):
        self.network_topology.append([s, d, w]) # List of distance from each node to rest of the nodes
        # print(self.network_topology)

    # Distance vector of each node
    def node_dv(self, distance):
        print("Distance vector for node %a:%s" % ((column_names[i]), distance))


    def bellman_ford(self, src):

        # Initialize distance from source to all other nodes/edges
        distance = [float("Inf")] * self.nodes
        distance[column_names.index(src)] = 0

        # To determine shortest path all weight cycles are positive
        for _ in range(self.nodes - 1):
            for s, d, w in self.network_topology:
                if distance[column_names.index(s)] != float("Inf") and distance[column_names.index(s)] + w < distance[
                    column_names.index(d)]:
                    distance[column_names.index(d)] = distance[column_names.index(s)] + w

        # To handle negative weight cycles
        for s, d, w in self.network_topology:
            if distance[column_names.index(s)] != float("Inf") and distance[column_names.index(s)] + w < distance[
                column_names.index(d)]:
                print("Network contains negative weight cycle")
                return

        self.node_dv(distance)


if __name__ == "__main__":
    dijkstra()
    import_file()
    n = Network(len(column_names))
    for c in range(len(column_names)):
        for j in range(len(column_names)):
            n.nodesdistance(column_names[c], column_names[j], int(all_distances[column_names[c]][column_names[j]]))



    for i in range(len(column_names)):
        n.bellman_ford(column_names[i])
