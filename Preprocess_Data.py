import csv
import statistics 
import operator

#Preprocessing: Groups every five data points (assume sorted by X Value) in succession and keeps only the median value in the group.
#Experimental: May leave out outliers

#A future version should feature a "similarity check"

def oddMedian(datacluster):
    datacluster = sorted(datacluster, key = operator.itemgetter(1)) #Sort the data group by y-value
    return datacluster[int(len(datacluster)/2)] #Return the one in the middle

#Enter desired filename here
filename = "DIODE TEST 2020-10-07"

trimmed = open("Photodiode Test Data/Trimmed_{}.txt".format(filename),"w")
with open("Photodiode Test Data/{}.txt".format(filename), newline='') as csvfile:
    
    datafile = csv.reader(csvfile, delimiter=':')
    rowcount = 0

    datacluster = [] #Temporary Variable used to store a cluster of 5 data points in succession
    
    for row in datafile:
        if row[0] == "testStarted":
            print("begin")
            trimmed.write("testStarted\n")
        else:
            rowcount += 1 #For every row of data add 1 count
            if rowcount%5: #For when there are less than 5 data points
                datacluster.append((row[0],row[1])) #Append current row to datacluster
            else:
                datacluster.append((row[0],row[1])) #Append current row to datacluster
                trimmed.write(str(oddMedian(datacluster)[0])+":"+str(oddMedian(datacluster)[1])+"\n") #Write the median to the trimmed file
                datacluster=[] #Clear the cluster
    if (len(datacluster)>0):
        trimmed.write(str(oddMedian(datacluster)[0])+":"+str(oddMedian(datacluster)[1])+"\n") #Process the remaining points in the cluster
trimmed.close()

