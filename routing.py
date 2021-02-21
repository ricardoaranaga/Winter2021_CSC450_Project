import csv

# globals
DEBUG = True
topology = []
nodesDict = {}

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

# initializing step
N.append(source)
for n in range(1,len(nodesDict)+1):
    cost = topology[nodesDict[source]][n]
    w = topology[nodesDict[source]][0]
    v = topology[0][n]
    D[v] = cost
    if DEBUG: print("cost {} from {} to {}".format(cost,w,v))

#del D[source]

if DEBUG:
    print(('-'*30)+'STEP 0'+('-'*30))
    print(N)
    print(D)
    print('-'*66)

# Repeating step
counter = 1
while(counter < len(D)):
    if DEBUG: print("#################### Step:{}, {} ####################".format(counter,source))
    
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
        if DEBUG: 
            print("from {} to {} cost {}".format(w,v,cost))
            print("current v={} with cost={}".format(v,D[v])) 
        D[v] = min(int(D[v]),int(D[w])+int(cost))   
        if DEBUG: print("updated v={} with cost={}".format(v,D[v]))
        
    counter += 1

print("Shortest path tree for node {}:".format(source))
print(N)
print("Costs of the least-cost paths for node {}:".format(source))
print(str(D))