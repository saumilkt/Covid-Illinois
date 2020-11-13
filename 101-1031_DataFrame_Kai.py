import pandas as pd

df_cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')

df_cases = df_cases.query('Province_State == "Illinois"')
df_deaths = df_deaths.query('Province_State == "Illinois"')

filter = ['Admin2', 'Lat', 'Long_']
for i in range(1, 16):
    filter.append('10/' + str(i) + '/20') 

df_cases =  df_cases[filter]
df_deaths = df_deaths[filter]