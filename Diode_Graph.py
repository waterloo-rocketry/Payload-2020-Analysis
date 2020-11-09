import csv
import datetime

import numpy as np
import pandas as pd
import plotly.express as px


millisecondToHour = 60*60*1000 #Conversion Factor from millisecond to minute 
millisecondToMinute = 60*1000 #Conversion Factor from millisecond to minute 
millisecondToSecond = 1000 #Conversion Factor from millisecond to second
with open("Photodiode_Test_Data/DIODE1.txt", newline='') as csvfile:
    timeArray = []
    dataArray = []
    data = csv.reader(csvfile, delimiter=':')
    count = 0
    for row in data:
        count += 1
        if row[0] == "testStarted":
            print("begin")
            if not timeArray == []:
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
            #insert some functionality here in the future (if needed); it does nothing currently.
        else:
                    t = int(row[0])
                    hour = int(t/millisecondToHour)
                    min = int(t%millisecondToHour/millisecondToMinute)
                    sec = int((t%millisecondToHour%millisecondToMinute)/millisecondToSecond)
                    mic = t%millisecondToSecond*millisecondToSecond
                    readTime = datetime.time(hour=hour, minute=min, second=sec, microsecond=mic)
                    readBoard = row[1]
                    timeArray.append(readTime)
                    dataArray.append(readBoard)


df = pd.DataFrame(dict(time=timeArray, volt=dataArray))
fig = px.scatter(df, x=timeArray, y=dataArray)
fig.update_layout(
    title="Voltage v Time",
    xaxis_title="Minute:Second:Microsecond",
    yaxis_title="Volt"
)
fig.show()