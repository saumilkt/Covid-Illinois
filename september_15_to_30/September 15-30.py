#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# 9-15
df_9_15 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-15-2020.csv')

for index, row in df_9_15.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_15.drop(index, inplace=True)
        
for index, row in df_9_15.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_15.drop(index, inplace=True)    


# In[3]:


# 9-16
df_9_16 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-16-2020.csv')

for index, row in df_9_16.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_16.drop(index, inplace=True)
        
for index, row in df_9_16.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_16.drop(index, inplace=True)    


# In[4]:


# 9-17
df_9_17 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-17-2020.csv')

for index, row in df_9_17.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_17.drop(index, inplace=True)
        
for index, row in df_9_17.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_17.drop(index, inplace=True)     


# In[5]:


# 9-18
df_9_18 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-18-2020.csv')

for index, row in df_9_18.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_18.drop(index, inplace=True)
        
for index, row in df_9_18.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_18.drop(index, inplace=True)    


# In[6]:


# 9-19
df_9_19 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-19-2020.csv')

for index, row in df_9_19.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_19.drop(index, inplace=True)
        
for index, row in df_9_19.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_19.drop(index, inplace=True)   


# In[7]:


# 9-20
df_9_20 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-20-2020.csv')

for index, row in df_9_20.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_20.drop(index, inplace=True)
        
for index, row in df_9_20.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_20.drop(index, inplace=True)


# In[8]:


# 9-21
df_9_21 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-21-2020.csv')

for index, row in df_9_21.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_21.drop(index, inplace=True)
        
for index, row in df_9_21.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_21.drop(index, inplace=True)


# In[10]:


# 9-22
df_9_22 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-22-2020.csv')

for index, row in df_9_22.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_22.drop(index, inplace=True)
        
for index, row in df_9_22.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_22.drop(index, inplace=True)


# In[11]:


# 9-23
df_9_23 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-23-2020.csv')

for index, row in df_9_23.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_23.drop(index, inplace=True)
        
for index, row in df_9_23.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_23.drop(index, inplace=True)


# In[12]:


# 9-24
df_9_24 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-24-2020.csv')

for index, row in df_9_24.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_24.drop(index, inplace=True)
        
for index, row in df_9_24.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_24.drop(index, inplace=True)


# In[13]:


# 9-25
df_9_25 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-25-2020.csv')

for index, row in df_9_25.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_25.drop(index, inplace=True)
        
for index, row in df_9_25.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_25.drop(index, inplace=True)


# In[14]:


# 9-26
df_9_26 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-26-2020.csv')

for index, row in df_9_26.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_26.drop(index, inplace=True)
        
for index, row in df_9_26.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_26.drop(index, inplace=True)


# In[15]:


# 9-27
df_9_27 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-27-2020.csv')

for index, row in df_9_27.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_27.drop(index, inplace=True)
        
for index, row in df_9_27.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_27.drop(index, inplace=True)


# In[16]:


# 9-28
df_9_28 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-28-2020.csv')

for index, row in df_9_28.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_28.drop(index, inplace=True)
        
for index, row in df_9_28.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_28.drop(index, inplace=True)


# In[17]:


# 9-29
df_9_29 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-29-2020.csv')

for index, row in df_9_29.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_29.drop(index, inplace=True)
        
for index, row in df_9_29.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_29.drop(index, inplace=True)


# In[18]:


# 9-30
df_9_30 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-30-2020.csv')

for index, row in df_9_30.iterrows():
    if (not('US' in row['Country_Region'])):
        df_9_30.drop(index, inplace=True)
        
for index, row in df_9_30.iterrows():
    if (not('Illinois' in row['Province_State'])):
        df_9_30.drop(index, inplace=True)

