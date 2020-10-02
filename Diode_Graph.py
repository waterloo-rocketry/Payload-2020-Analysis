import numpy as np
import csv
import plotly.express as py
import pandas as pd
import datetime
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
            min = int(t/59000000)
            sec = int((t-(59000000*min))/999999)
            mic = int ((t-(59000000*min)-(999999*sec)))
            readTime = datetime.time(minute=min, second=sec, microsecond=mic)
            readBoard = row[1]
            timeArray.append(readTime)
            dataArray.append(readBoard)
    df = pd.DataFrame(dict(time=timeArray, volt=dataArray))
    fig = py.scatter(df, x=timeArray, y=dataArray)
    fig.update_layout(
    title="Voltage v Time",
    xaxis_title="Time",
    yaxis_title="Voltage"
    )
    fig.show()

