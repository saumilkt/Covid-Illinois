#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# 
# df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
# df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')

# IL_df_confirmed = df_confirmed.query('Province_State == "Illinois"')
# IL_df_deaths = df_deaths.query('Province_State == "Illinois"')

# filter1 = ['Admin2', 'Lat', 'Long_']

# filter2 = ['Admin2', 'Lat', 'Long_']

# for i in range(24, 31):
#     filter1.append('8/' + str(i) + '/20')

# for j in range(1, 15):
#     filter2.append('9/' + str(j) + '/20')

# IL_df_confirmed_aug24_sept15 = IL_df_confirmed[filter1] + IL_df_confirmed[filter2]
# IL_df_deaths_aug24_sept15 = IL_df_deaths[filter1] + IL_df_deaths[filter2]
