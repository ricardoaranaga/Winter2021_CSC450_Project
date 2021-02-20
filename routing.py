import csv

DEBUG = True
topology = []
nodesDict = {}

with open('topology-1.csv', newline='') as file:
     cvsReader = csv.reader(file, delimiter=',')
     for row in cvsReader:
         if DEBUG: print(row)
         topology.append(row)


for i in range(1,len(topology[0])):
    nodesDict[topology[0][i]] = i

if DEBUG: print(nodesDict)

source = input("Please, provide the source node: ")

if DEBUG: 
    print('-'*50)
    print("Text entered:{} / source node:{} / value:{}".format(source,source,nodesDict[source])) 
    print('-'*50)

# initializing step
for n in range(1,len(nodesDict)+1):
    cost = topology[nodesDict[source]][n]
    src = topology[nodesDict[source]][0]
    dest = topology[0][n]
    print("cost {} from {} to {}".format(cost,src,dest))

