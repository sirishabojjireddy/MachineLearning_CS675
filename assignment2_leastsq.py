import sys
import math
import random 

# Defining Dot Product Function
def dot(w,data):
    ans=0
    for j in range(0,len(w),1):
        ans = ans + w[j]*data[j]
    return ans


# Reading in Data file
dfile = sys.argv[1]
f = open(dfile)
data = []
i = 0
l = f.readline()

while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
    
r = len(data)
c = len(data[0])
f.close



# Reading Label File 
labfile = sys.argv[2]
f = open(labfile)
trainlabels = {}
l = f.readline()
n=[]
n.append(0)
n.append(0)

while(l != ''):
    a= l.split()
    trainlabels[int(a[1])] = int(a[0])
    if(trainlabels[int(a[1])] == 0):
        trainlabels[int(a[1])] = -1
    l = f.readline()
    n[int(a[0])] += 1
    

w = []
# initalizing w 
for j in range(0,c):
    w.append(random.uniform(-.01, .01))



#setting eta and stopping condition 
#gradient descent iteration
eta=0.0001
stop_condition=0.001
error=0
prevobj = 10000000
error = prevobj - 10
while True:
    prevobj=error
    
    #reset dellf to 0
    dellf = []
    for j in range(0, c):
        dellf.append(0)

    #compute gradient and error
    error=0

    for i in range (0,r,1):
        if (trainlabels.get(i) != None):
            dp=dot(w,data[i])
            error += (trainlabels[i] - dp)**2

            for j in range (0,c,1):
                dellf[j] += (trainlabels[i]-dp)*data[i][j]

    if prevobj-error<=stop_condition:
        break 

    #update w
    for j in range (0,c,1):
        w[j]=w[j]+eta*dellf[j]
    
#    print("objective is:", error)


#print("w = ", w)

normw = 0
for j in range (0, (c-1), 1):
    normw += w[j]**2
 #   print(f'w{j}: {abs(w[j])}')
    
normw = math.sqrt(normw)
origin_distance = abs(w[len(w)-1]/normw)
print ("Distance from Origin= ", origin_distance)


for i in range (0, r):
    if (trainlabels.get(i) == None):
        dp = 0
        for j in range (0, c):
            dp += data[i][j]*w[j]
        if dp > 0:
            print ("1", i)
        else:
            print ("0", i)

