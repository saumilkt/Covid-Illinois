import pandas as pd
import dataframes as data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
import mpld3

mpld3.enable_notebook()
df = data.createdf()

#county = input("Input an Illinois County: ")
county = "Cook"
queryFilter = "Admin2 == \"" + county + "\""
df_county = df.query(queryFilter)

dates = []

for dat in df_county.Last_Update:
    dates.append(datetime.datetime.strptime(dat, '%Y-%m-%d %H:%M:%S'))

pltdates = mdates.date2num(dates)
plt.plot(dates,df_county["Confirmed"], label='Confirmed Cases')
plt.plot(dates,df_county["Case-Fatality_Ratio"], label='Case-Fatality Ratio')
plt.plot(dates,df_county["Deaths"], label='Deaths')

plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Number of Cases')
title = county + " County Covid Cases"
plt.title(title)
plt.legend()
