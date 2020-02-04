import sys
import math

dfile = sys.argv[1]
f = open(dfile)
data = []
i = 0
l = f.readline()

# Reading data

while(l != ''):
    x = l.split()
    l2 = []
    for j in range(0, len(x), 1):
        l2.append(float(x[j]))
    data.append(l2)
    l = f.readline()
    
r = len(data)
c = len(data[0])
f.close

# Reading label file 
labfile = sys.argv[2]
f = open(labfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()

#Count total number of records
while(l != ''):
    x= l.split()
    trainlabels[int(x[1])] = int(x[0])
    l = f.readline()
    n[int(x[0])] += 1
    
    
mean0 = []
for j in range(0, c, 1):
    mean0.append(.01)
    
mean1 = []
for j in range(0, c, 1):
    mean1.append(.01)
     
for i in range(0, r, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, c, 1):
            mean0[j] = mean0[j] + data[i][j]
            
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(0, c, 1):
            mean1[j] = mean1[j] + data[i][j]

#Find Means
for j in range(0, c, 1):
    mean0[j] = mean0[j]/n[0]
    mean1[j] = mean1[j]/n[1]



sd0 = []
sd1 = []

for j in range(0, c, 1):
    sd0.append(0)
    sd1.append(0)
    

for i in range(r):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, c, 1):
            sd0[j] += (data[i][j] - mean0[j]) ** 2
        
    
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(0, c, 1):
            sd1[j] += (data[i][j] - mean1[j]) ** 2
            

for i in range(c):
    sd0[i] = sd0[i]/ n[0]
    sd1[i] = sd1[i]/ n[1]
    
for i in range(0, r, 1):
    if(trainlabels.get(i) == None):
        dm0 = 0
        dm1 = 0
        for j in range( 0, c, 1):
            dm0 = dm0 + ((data[i][j] - mean0[j])**2 / (sd0[j]))
            dm1 = dm1 + ((data[i][j] - mean1[j])**2 / (sd1[j]))
        
        if(dm0 < dm1):
            print("0", i)
        
        else:
            print("1", i)






