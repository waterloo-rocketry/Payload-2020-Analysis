import csv
import statistics 
import operator

#Preprocessing: Groups every five data points (assume sorted by X Value) in succession and keeps only the median value in the group.
#Experimental: May leave out outliers

#A future version should feature a "similarity check"

def oddMedian(datacluster):
    datacluster = sorted(datacluster, key = operator.itemgetter(1)) #Sort the data group by y-value
    return datacluster[int(len(datacluster)/2)] #Return the one in the middle

def tangentialSimilarity(datacluster, cutoffslope, filestream): #cutoff is arbitrary
    sortedcluster = sorted(datacluster, key = operator.itemgetter(1)) #Sort the data group by y-value
    medianx = float(datacluster[int(len(datacluster)/2)][0]) #Find the corresponding x value of the median
    mediany = float(datacluster[int(len(datacluster)/2)][1]) #Find the median y value
    
    for i in range(len(datacluster)):
        if (i == int(len(datacluster)/2)):
            filestream.write(str(int(medianx))+" : "+str(mediany)+"\n") #If the median is iterated, write to file
        elif (abs((float(datacluster[i][1])-mediany)/(float(datacluster[i][0]) - medianx))>cutoffslope): #Check if the abs value of the slope is greater
            filestream.write(datacluster[i][0]+":"+datacluster[i][1]+"\n") #If is then write to file

#Enter desired filename here
filename = "DIODE TEST 2020-10-07"

trimmed = open("Photodiode Test Data/TrimmedV2_{}.txt".format(filename),"w")
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
                tangentialSimilarity(datacluster, 0.1, trimmed) #Arbitrary Cutoff Value; delta y/delta x
                #trimmed.write(str(oddMedian(datacluster)[0])+":"+str(oddMedian(datacluster)[1])+"\n") #Write the median to the trimmed file
                datacluster=[] #Clear the cluster
    if (len(datacluster)>0):
        tangentialSimilarity(datacluster, 0.1, trimmed)
        #trimmed.write(str(oddMedian(datacluster)[0])+":"+str(oddMedian(datacluster)[1])+"\n") #Process the remaining points in the cluster
print("end")
trimmed.close()

