import csv
import statistics 
import operator
from rdp import rdp
import numpy as np

#DO NOT TOUCH ---------- WIP
#DOES NOT WORK YET, DO NOT ATTEMPT TO RUN IT

#Enter desired filename here
filename = "DIODE1"
dataArray = []
trimmed = open("Photodiode Test Data/RDPTrimmed_{}.txt".format(filename),"w")
with open("Photodiode Test Data/{}.txt".format(filename), newline='') as csvfile:
    
    datafile = csv.reader(csvfile, delimiter=':')
    
    for row in datafile:
        if row[0] == "testStarted":
            print("begin")
            trimmed.write("testStarted\n")
        else:
            dataArray.append([row[0],row[1]]) #Append current row to dataarray

processedArray = rdp(dataArray, algo="iter", return_mask=False)

for i in processedArray:
    trimmed.write(processedArray[i][0]+":"+processedArray[i][1]+"\n")

print("end")
trimmed.close()

