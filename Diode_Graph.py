import csv
import datetime

import numpy as np
import plotly.express as px
import pandas as pd

microsecondToMinute = 60000000 #Conversion Factor from microsecond to minute 
microsecondToSecond = 1000000 #Conversion Factor from microsecond to second
with open("DIODE1.txt", newline='') as csvfile:
    timeArray = []
    dataArray = []
    data = csv.reader(csvfile, delimiter=':')
    for row in data:
        if(row[0] == "testStarted"):
            print("begin")
            #do something idk what yet
        else:
            t = int(row[0])
            min = int(t/microSecondToMinute)
            sec = int((t%microSecondToMinute)/microsecondToSecond)
            mic = t%microsecondToSecond
            readTime = datetime.time(minute=min, second=sec, microsecond=mic)
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

