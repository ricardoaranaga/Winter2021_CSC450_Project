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


class Network:
    def __init__(self, nodes_count):

        self.nodes = nodes_count  # Total number of nodes in the network_topology
        self.network_topology = []  # Array of nodes

    # Add edges
    def add_edge(self, s, d, w):
        self.network_topology.append([s, d, w])

    # Print the solution
    def print_solution(self, distance):
        print("\nDistance vector for node %a:%s" % ((column_names[i]), distance))
        # for i in range(self.nodes):
        #   print("{0}\t\t{1}".format(column_names[i], distance[i]))

    def bellman_ford(self, src):

        distance = [float("Inf")] * self.nodes

        distance[column_names.index(src)] = 0

        for _ in range(self.nodes - 1):
            for s, d, w in self.network_topology:
                if distance[column_names.index(s)] != float("Inf") and distance[column_names.index(s)] + w < distance[
                    column_names.index(d)]:
                    distance[column_names.index(d)] = distance[column_names.index(s)] + w

        for s, d, w in self.network_topology:
            if distance[column_names.index(s)] != float("Inf") and distance[column_names.index(s)] + w < distance[
                column_names.index(d)]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(distance)


if __name__ == "__main__":
    import_file()
    n = Network(len(column_names))
    for c in range(len(column_names)):
        for j in range(len(column_names)):
            n.add_edge(column_names[c], column_names[j], int(all_distances[column_names[c]][column_names[j]]))
            # print(column_names[i],column_names[j],distances[column_names[i]][column_names[j]])

    # g.read_file()
    for i in range(len(column_names)):
        n.bellman_ford(column_names[i])
