import pandas as pd

def createdf():
    filter = ['Admin2', 'Lat', 'Long_', 'Last_Update', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Incidence_Rate', 'Case-Fatality_Ratio']

    for i in range(7,12):
        for j in range(31):
            tempAddressMonth = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

            if i + 1 < 10:
                tempAddressMonth = tempAddressMonth + "0" + str(i+1)
            else:
                tempAddressMonth = tempAddressMonth + str(i+1)

            tempAddressDay = tempAddressMonth + "-"

            if j + 1 < 10:
                tempAddressDay = tempAddressDay + "0" + str(j+1)
            else:
                tempAddressDay = tempAddressDay + str(j+1)
            
            tempAddressDay = tempAddressDay + "-2020.csv"

            try:
                temp_df = pd.read_csv(tempAddressDay)

                temp_df = temp_df.query('Province_State == "Illinois"')
                temp_df = temp_df.query('Country_Region == "US"')

                temp_df = temp_df.rename(columns = {"Incident_Rate":"Incidence_Rate"})
                temp_df = temp_df.rename(columns = {"Case_Fatality_Ratio":"Case-Fatality_Ratio"})
                temp_df = temp_df[filter]
                if i == 7 and j == 0:
                    df = temp_df
                else:
                    df = pd.concat([df,temp_df])
                print("Data for " + str(i + 1) + "/" + str(j + 1) + " added")
            except IOError as e:
                i = i
                j = j

    print("Done creating dataframes")
    return df