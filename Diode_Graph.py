import csv
import datetime

import numpy as np
import plotly.express as px
import pandas as pd

millisecondToHour = 60*60*1000 #Conversion Factor from millisecond to hour
millisecondToMinute = 60*1000 #Conversion Factor from microsecond to minute 
millisecondToSecond = 1000 #Conversion Factor from microsecond to second

with open("DIODE3.txt", newline='') as csvfile:
    timeArray = []
    dataArray = []
    data = csv.reader(csvfile, delimiter=':')
    count = 0
    for row in data:
        count += 1
        if row[0] == "testStarted":
            print("begin")
            #insert some functionality here in the future (if needed); it does nothing currently.
        else:
            if count%5000000:
                if float(row[1]) > 1.13:
                    t = int(row[0])
                    hour = int(t/millisecondToHour)
                    min = int(t%millisecondToHour/millisecondToMinute)
                    sec = int((t%millisecondToHour%millisecondToMinute)/millisecondToSecond)
                    mic = t%millisecondToSecond*1000
                    readTime = datetime.time(hour=hour, minute=min, second=sec, microsecond=mic)
                    readBoard = row[1]
                    timeArray.append(readTime)
                    dataArray.append(readBoard)
            else:
                df = pd.DataFrame(dict(time=timeArray, volt=dataArray))
                fig = px.scatter(df, x=timeArray, y=dataArray)
                fig.update_layout(
                    title="Voltage v Time",
                    xaxis_title="Minute:Second:Microsecond",
                    yaxis_title="Volt"
                )
                fig.show()
                timeArray = []
                dataArray = []

df = pd.DataFrame(dict(time=timeArray, volt=dataArray))
fig = px.scatter(df, x=timeArray, y=dataArray)
fig.update_layout(
    title="Voltage v Time",
    xaxis_title="Minute:Second:Microsecond",
    yaxis_title="Volt"
)
fig.show()