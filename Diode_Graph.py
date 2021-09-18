import csv
import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import converttocsv as conv

# set path to logfile in wack format here
file_path = "./logfile_dump/log.txt"

# generate a CSV from that wack file
conv.main(file_path)

# enter desired filename
filename = "based"

# decide whether 

millisecondToHour = 60*60*1000 #Conversion Factor from millisecond to minute 
millisecondToMinute = 60*1000 #Conversion Factor from millisecond to minute 
millisecondToSecond = 1000 #Conversion Factor from millisecond to second
with open(f"Photodiode_Test_Data/{filename}.csv") as csvfile:
    timeArray = []
    peakArray = []
    signalArray = []
    #count = 0  --- Debug Tool
    data = csv.reader(csvfile, delimiter=':')
    #sections = 0   --- Debug Tool
    for row in data:
        if row[0] == "testStarted":
            print("begin")
        else:
            t = int(row[2])
            hour = int(t / millisecondToHour)
            minute = int(t % millisecondToHour / millisecondToMinute)
            sec = int((t % millisecondToHour % millisecondToMinute) / millisecondToSecond)
            mic = t % millisecondToSecond * millisecondToSecond #MillisecondToSecond = MicrosecondToSecond = 1000
            readTime = datetime.time(hour = hour, minute = minute, second = sec, microsecond = mic)

            readPeak = row[0]
            readSig = row[1]
            timeArray.append(readTime)
            signalArray.append(readSig)
            peakArray.append(readPeak)

df = pd.DataFrame(dict(time=timeArray, signal=signalArray, peak=peakArray))

# change the y variable to show peak array or signal array
fig = px.scatter(df, x=timeArray, y=peakArray)
fig.update_layout(
    title="Voltage v Time",
    xaxis_title="Hour:Minute:Second:Microsecond",
    yaxis_title="Volt"
)
fig.write_html("graph/GRAPH-{}.html".format(filename))
