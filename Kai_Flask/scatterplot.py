import pandas as pd
import dataframes as data
import matplotlib.pyplot as plt
import numpy as np
import mpld3

def create_scatter(day, month, stat):
    title = month + '-' + day + '_' + stat + '.png'

    df = data.createdf_date(month, day)
    df.drop(df.index[df['Admin2'] == 'Cook'], inplace = True)
    df.drop(df.index[df['Admin2'] == 'Unassigned'], inplace = True)
    df.drop(df.index[df['Admin2'] == 'Out of IL'], inplace = True)

    max = df[stat].max()
    scale = df[stat]/max

    fig, sub = plt.subplots()
    img=plt.imread('map/illinois_county.png')

    plt.imshow(img,zorder=0,extent=[df['Long_'].min()-0.3,df['Long_'].max()+0.25,df['Lat'].min()-0.2,df['Lat'].max()+0.18])
    ax = plt.gca()
    scatter = sub.scatter(x = df['Long_'], y = df['Lat'], c = scale, cmap = plt.get_cmap("jet"), s = scale*3000 , alpha = 0.5, zorder=5)

    ax.set_ylim([36.5,43])
    ax.set_xlim([-92.8,-86])

    labels = df['Admin2'].to_numpy()
    labels = labels.tolist()

    statLabels = df[stat].to_numpy()
    statLabels = statLabels.tolist()

    for x in range(len(labels)):
        labels[x] = labels[x] + ': ' + str(statLabels[x])

    tooltips = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltips)

    saveLocation = 'Kai_Flask/static/plots/' + title

    plt.savefig(saveLocation)
    return title