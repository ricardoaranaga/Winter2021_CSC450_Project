import csv
import sys

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
N.append(source)
for n in range(1,len(nodesDict)+1):
    cost = topology[nodesDict[source]][n]
    w = topology[nodesDict[source]][0]
    v = topology[0][n]
    D[v] = cost
    SP[v] = source
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
    
    temp_D = {key:val for key, val in D.items() if key not in N}
    if len(temp_D) > 0:
        temp = min(temp_D, key=temp_D.get)
        if DEBUG: print("Minimum={}, with={}".format(temp,D[temp]))
    
    N.append(temp)
    if DEBUG: print(N)

    for n in range(1,len(D)+1):
        cost = topology[nodesDict[temp]][n]
        w = topology[nodesDict[temp]][0]
        v = topology[0][n]
        previous = int(D[v])
        new = int(D[w])+int(cost)
        D[v] = min(previous,new)
        if DEBUG: 
            print("from {} to {} cost {}".format(w,v,cost))
            print("previous v={} with cost={}".format(v,previous)) 
            print("updated v={} with cost={}".format(v,new))
        
        if new < previous:
            SP[v] = SP[w] + w
            if DEBUG: print("CHANGED({}) {}".format(v,SP[v]))

    counter += 1

# building the shortest path string
del SP[source]
shortestPath = ""
for node in SP:
    shortestPath += node+': '+SP[node]+node+', '
shortestPath = shortestPath[:-2]

# print resulting outputs
print("Shortest path tree for node {}:".format(source))
print(shortestPath)
print("Costs of the least-cost paths for node {}:".format(source))
print(str(D).replace('{','').replace('}','').replace("'",""))
