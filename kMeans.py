#Assignment Information
#Name: Havan Patel
#Date: 12/23/2022
#Course Name: Statistical Programming
#Semester: Spring 2022
#Programming Assignment #2

print("Data 51100, Spring 2022")
print("Havan Patel")
print("Programming Assignment #2")

inputFile = input("Enter the name of the input file: ")
outputFile = input("Enter the name of the output file: ")
k = int(input("Enter a number of cluster: "))

file = open(inputFile, "r")

#read file
content = file.read()
points = [float(x) for x in content.splitlines()]
file.close()

#initialize variables
centroids = [points[i] for i in range(k)]
clusters = dict(zip(range(k), [[] for i in range(k)]))
distanceList = []

# calculate distance
def getDistance(p, q):
    return abs(p - q)

# put points from centroids into the cluster by getting the min distance 
def assign_to_clusters(centroids):
    global clusters
    #reset cluster to empty for new ones
    clusters = dict(zip(range(k), [[] for i in range(k)]))
    distanceList = []
    #go through all the points in file
    for x in range(len(points)):
        #assign max disance for now
        smallesDistance = 99999999999999999999999999
        #need this to know which cluster the point belongs to
        smallesDistanceIndex = 0
        #go through all the clusters
        for y in range(0, k):
            # get distance from points in file to points centroid to see which cluster it will go to 
            currentDistance = getDistance(points[x], centroids[y])
            # add to distance list
            distanceList.append(currentDistance)
            # get the minimum distance
            # if current distance is less then smallest distance, we know it belongs to this cluster
            if currentDistance < smallesDistance:
                smallesDistance = currentDistance
                smallesDistanceIndex = y
        # assign the point to this cluster
        clusters[smallesDistanceIndex].append(points[x])
    #return the list of all distance
    return distanceList

def update_centeroid(centroids):
    # get sum of values in each clusterand take average of it
    new_centroids = {k: sum(value) / float(len(value)) for k, value in clusters.items()}
    return new_centroids

distanceList = assign_to_clusters(centroids)

currentDistanceList = distanceList 
itr = 0
oldDistanceList = []
# continue until distance are different
while distanceList != oldDistanceList:
    itr += 1
    print("\n")
    print("Iteration ", itr)
    [print(index, '', value) for index, value in clusters.items()]
    centroids = update_centeroid(centroids)
    currentDistanceList = distanceList
    oldDistanceList = currentDistanceList
    distanceList = assign_to_clusters(centroids)

print("\n")

#write output to file
outFile = open(outputFile, "a")
for i in range(len(points)):
    for j in range(k):
        # check in which cluster the data point is in
        if points[i] in clusters[j]:
            print("Point "+str(points[i])+" in cluster "+str(j))
            outFile.write("Point "+str(points[i])+" in cluster "+str(j)+"\n")
outFile.close()
