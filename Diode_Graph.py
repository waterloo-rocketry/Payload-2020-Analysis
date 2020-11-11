import csv
import datetime
import numpy as np
import pandas as pd
import plotly.express as px
#Enter desired filename here
filename = "DIODE-2020-11-06"


millisecondToHour = 60*60*1000 #Conversion Factor from millisecond to minute 
millisecondToMinute = 60*1000 #Conversion Factor from millisecond to minute 
millisecondToSecond = 1000 #Conversion Factor from millisecond to second
with open("test_data/{}.txt".format(filename), newline='') as csvfile:
    timeArray = []
    dataArray = []
    count = 0
    data = csv.reader(csvfile, delimiter=':')
    sections = 0
    for row in data:
        if row[0] == "testStarted":
            print("begin")
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
    xaxis_title="Hour:Minute:Second:Microsecond",
    yaxis_title="Volt"
)
fig.write_html("graph/GRAPH-{}.html".format(filename))