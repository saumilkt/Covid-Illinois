#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt, mpld3
import matplotlib as mp
import numpy as np


# In[22]:


df_824_915_dates = []


# In[23]:


df_8_24 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-24-2020.csv')

for index, row in df_8_24.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_24.drop(index, inplace=True)
        
for index, row in df_8_24.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_24.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_24)


# In[24]:


df_8_25 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-25-2020.csv')

for index, row in df_8_25.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_25.drop(index, inplace=True)
        
for index, row in df_8_25.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_25.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_25)


# In[25]:


df_8_26 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-26-2020.csv')

for index, row in df_8_26.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_26.drop(index, inplace=True)
        
for index, row in df_8_26.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_26.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_26)


# In[26]:


df_8_27 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-27-2020.csv')

for index, row in df_8_27.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_27.drop(index, inplace=True)
        
for index, row in df_8_27.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_27.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_27)


# In[27]:


df_8_28 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-28-2020.csv')

for index, row in df_8_28.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_28.drop(index, inplace=True)
        
for index, row in df_8_28.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_28.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_28)


# In[28]:


df_8_29 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-29-2020.csv')

for index, row in df_8_29.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_29.drop(index, inplace=True)
        
for index, row in df_8_29.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_29.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_29)


# In[29]:


df_8_30 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-30-2020.csv')

for index, row in df_8_30.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_30.drop(index, inplace=True)
        
for index, row in df_8_30.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_30.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_30)


# In[30]:


df_8_31 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-31-2020.csv')

for index, row in df_8_31.iterrows():
    if (not('US' in row['Country_Region'])):
        df_8_31.drop(index, inplace=True)
        
for index, row in df_8_31.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_8_31.drop(index, inplace=True)
        
df_824_915_dates.append(df_8_31)


# In[31]:


df_9_01 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-01-2020.csv')

for index, row in df_9_01.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_01.drop(index, inplace=True)
        
for index, row in df_9_01.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_01.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_01)


# In[32]:


df_9_02 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-02-2020.csv')

for index, row in df_9_02.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_02.drop(index, inplace=True)
        
for index, row in df_9_02.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_02.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_02)


# In[33]:


df_9_03 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-03-2020.csv')

for index, row in df_9_03.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_03.drop(index, inplace=True)
        
for index, row in df_9_03.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_03.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_03)


# In[34]:


df_9_04 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-04-2020.csv')

for index, row in df_9_04.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_04.drop(index, inplace=True)
        
for index, row in df_9_04.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_04.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_04)


# In[35]:


df_9_05 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-05-2020.csv')

for index, row in df_9_05.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_05.drop(index, inplace=True)
        
for index, row in df_9_05.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_05.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_05)


# In[36]:


df_9_06 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-06-2020.csv')

for index, row in df_9_06.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_06.drop(index, inplace=True)
        
for index, row in df_9_06.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_06.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_06)


# In[37]:


df_9_07 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-07-2020.csv')

for index, row in df_9_07.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_07.drop(index, inplace=True)
        
for index, row in df_9_07.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_07.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_07)


# In[38]:


df_9_08 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-08-2020.csv')

for index, row in df_9_08.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_08.drop(index, inplace=True)
        
for index, row in df_9_08.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_08.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_08)


# In[39]:


df_9_09 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-09-2020.csv')

for index, row in df_9_09.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_09.drop(index, inplace=True)
        
for index, row in df_9_09.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_09.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_09)


# In[40]:


df_9_10 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-10-2020.csv')

for index, row in df_9_10.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_10.drop(index, inplace=True)
        
for index, row in df_9_10.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_10.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_10)


# In[41]:


df_9_11 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-11-2020.csv')

for index, row in df_9_11.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_11.drop(index, inplace=True)
        
for index, row in df_9_11.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_11.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_11)


# In[42]:


df_9_12 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-12-2020.csv')

for index, row in df_9_12.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_12.drop(index, inplace=True)
        
for index, row in df_9_12.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_12.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_12)


# In[43]:


df_9_13 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-13-2020.csv')

for index, row in df_9_13.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_13.drop(index, inplace=True)
        
for index, row in df_9_13.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_13.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_13)


# In[44]:


df_9_14 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-14-2020.csv')

for index, row in df_9_14.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_14.drop(index, inplace=True)
        
for index, row in df_9_14.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_14.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_14)


# In[45]:


df_9_15 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-15-2020.csv')

for index, row in df_9_15.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_15.drop(index, inplace=True)
        
for index, row in df_9_15.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_15.drop(index, inplace=True)
        
df_824_915_dates.append(df_9_15)


# In[46]:


plt.figure(figsize=(20,10))
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Number of Cases')
plt.ylim(top=140000)
plt.ylim(bottom=120000)
plt.title("Illinois Confirmed Covid Cases")
for i in range(0, 23):
    plt.plot(df_824_915_dates[i].Last_Update, df_824_915_dates[i].Confirmed, label='Confirmed Cases')


# In[47]:


for df in df_824_915_dates:
    for index, row in df.iterrows():
        if ('Unassigned') in row['Admin2']:
            df.drop(index, inplace = True)
        elif ('Out of IL') in row['Admin2']:
            df.drop(index, inplace = True)

df_824_915_dates = pd.concat(df_824_915_dates)
df_824_915_dates.set_index('Last_Update')
df_824_915_dates["Last_Update"] = pd.to_datetime(df_824_915_dates["Last_Update"])
print(df_9_15.Lat)


# In[48]:


df_9_15.set_index('Last_Update')


# In[49]:


fig = plt.figure(figsize=(16,9))
ax=fig.add_axes([0,0,1,1])
xs = df_9_15.Lat
ys = df_9_15.Long_
labels = df_9_15.Admin2
size = df_9_15.Incidence_Rate

cm = plt.cm.get_cmap('RdYlBu')
ax.scatter(x=xs, y=ys, c=size, s=size * 0.4, cmap=cm)
cb = plt.scatter(xs, ys, c=size, s=size * 0.4, cmap=cm)
ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.set_title("Incidence rate of Covid In Illinois Counties")

def label_point_orig(xs, ys, val, ax):
    a = pd.concat({'x': xs, 'y': ys, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))
plt.scatter(list(xs), list(ys))
label_point_orig(xs, ys, labels, plt)
plt.colorbar(cb)
mpld3.show()


# In[50]:


fig = plt.figure(figsize=(12,7))
ax=fig.add_axes([0,0,1,1])
xs = df_9_15.Long_
ys = df_9_15.Lat
labels = df_9_15.Admin2
size = df_9_15['Case-Fatality_Ratio']

cm = plt.cm.get_cmap('RdYlBu')
ax.scatter(x=ys, y=xs, c=size, s=size * 105, cmap=cm)
cb = plt.scatter(xs, ys, c=size, s=size * 105, cmap=cm)
ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.set_title("Case to Death Ratio to Covid In Illinois Counties")

def label_point_orig(xs, ys, val, ax):
    a = pd.concat({'x': xs, 'y': ys, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))
plt.scatter(list(xs), list(ys))
label_point_orig(xs, ys, labels, plt)
plt.colorbar(cb)

img = plt.imread("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPPTSPUryiWGww3MXCWMV_DA9e3tHwA-W8bA&usqp=CAU")
plt.imshow(img, zorder=0, extent = [-91.5, -87.4, 36.95, 42.55], origin="upper")
mpld3.display()


# In[ ]:


x axis, lowest income to highest income
y axis, cases to deaths



# In[76]:


df_IL_se = pd.read_excel('/Users/jiber1/Library/Containers/com.microsoft.Excel/Data/Downloads/Illinois-SocioEconomicData-Master (1).xlsx')

for index, row in df_IL_se.iterrows():
    if ('Unassigned') in row['Location']:
        df_IL_se.drop(index, inplace = True)
    elif ('Out of IL') in row['Location']:
        df_IL_se.drop(index, inplace = True)
    elif ('Illinois') in row['Location']:
        df_IL_se.drop(index, inplace = True)
print(df_IL_se)


# In[90]:


fig = plt.figure(figsize=(12,7))
ax=fig.add_axes([0,0,1,1])
xs = df_IL_se['Median household income (dollars)']
ys = df_9_15['Case-Fatality_Ratio']
labels = df_IL_se.Location

print(xs)
print(ys)

ax.scatter(xs, ys)
ax.set_xlabel("Median household income")
ax.set_ylabel("Case-Fatality Ration")
ax.set_title("Case to Death Ratio to Median income of Illinois Counties")
plt.show()



# In[ ]:





# In[ ]:




