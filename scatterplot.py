import pandas as pd
import dataframes as data
import matplotlib.pyplot as plt
import numpy as np
import mpld3

month = input("Input a month (mm): ")
day = input("Input a day (dd): ")
df = data.createdf_date(month, day)
df.drop(df.index[df['Admin2'] == 'Cook'], inplace = True)
df.drop(df.index[df['Admin2'] == 'Unassigned'], inplace = True)
df.drop(df.index[df['Admin2'] == 'Out of IL'], inplace = True)

max = df['Confirmed'].max()
scale = df['Confirmed']/max

fig, sub = plt.subplots()
img=plt.imread('map/illinois_county.png')

plt.imshow(img,zorder=0,extent=[df['Long_'].min()-0.3,df['Long_'].max()+0.25,df['Lat'].min()-0.2,df['Lat'].max()+0.18])
ax = plt.gca()
scatter = sub.scatter(x = df['Long_'], y = df['Lat'], c = scale, cmap = plt.get_cmap("jet"), s = scale*3000 , alpha = 0.5, zorder=5)

ax.set_ylim([36.5,43])
ax.set_xlim([-92.8,-86])

labels = df['Admin2'].to_numpy()
labels = labels.tolist()
tooltips = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltips)

mpld3.show()