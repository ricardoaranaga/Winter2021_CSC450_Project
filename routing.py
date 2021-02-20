import csv

# globals
DEBUG = True
topology = []
nodesDict = {}

# functions
def addMinToFinal():
  for node in N:
    if D.get(node) != None:
        final[node] = D.pop(node, 'No Key found')
        if DEBUG:
            print(('-'*30)+'ADDMIN'+('-'*30))
            print(final)
            print(D)
            print('-'*66)

# reading the csv file
with open('topology-1.csv', newline='') as file:
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
final = {}
# initializing step
N.append(source)
for n in range(1,len(nodesDict)+1):
    cost = topology[nodesDict[source]][n]
    src = topology[nodesDict[source]][0]
    v = topology[0][n]
    D[v] = cost
    if DEBUG: print("cost {} from {} to {}".format(cost,src,v))

addMinToFinal()

if DEBUG:
    print(('-'*30)+'STEP 0'+('-'*30))
    print(N)
    print(D)
    print('-'*66)

# Repeating step
while(len(nodesDict) > 0 ):
    print("###################### Current source: {} ######################".format(source))
    for n in range(1,len(topology[nodesDict[source]])):
        if len(D) == 0:
            print("#"*66)
            break
        cost = topology[nodesDict[source]][n]
        src = topology[nodesDict[source]][0]
        v = topology[0][n]
        # ToDo: update cost here

        # ####
        if DEBUG: print("cost {} from {} to {}".format(cost,src,v))
        print(D, len(D))
        temp = min(D.values()) 
        print("Minimum {}".format(temp))
        res = [key for key in D if D[key] == temp]
        if DEBUG: print("Keys with minimum values are: {}".format(res))
        N.append(res[0])
        print(N)

        addMinToFinal()

    del nodesDict[source]
    source = next(iter(nodesDict))
    for n in range(1,len(nodesDict)+1):
        cost = topology[nodesDict[source]][n]
        src = topology[nodesDict[source]][0]
        v = topology[0][n]
        D[v] = cost
        if DEBUG: print("cost {} from {} to {}".format(cost,src,v))

exit(0)






