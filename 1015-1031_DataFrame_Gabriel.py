import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
ill_df = df.query('Province_State == "Illinois"')
filter = ['Admin2', 'Lat', 'Long_']
for i in range(15, 32):
    filter.append('10/' + str(i) + '/20')   #Populate filter list with dates
ill_df_trimmed = ill_df[filter]
ill_df_trimmed
