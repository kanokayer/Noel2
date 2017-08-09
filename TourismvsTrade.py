# coding: utf-8
import pandas as pd
import numpy as np
databay = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//BayCounty.csv", usecols=[0,5])
databrevard = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//BrevardCounty.csv", usecols=[0,5])

databroward = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//BrowardCounty.csv", usecols=[0,5])

datacollier = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//CollierCounty.csv", usecols=[0,5])

dataduval = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//DuvalCounty.csv", usecols=[0,5])

dataescambia = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//EscambiaCounty.csv", usecols=[0,5])
datahillsborough = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//HillsboroughCounty.csv", usecols=[0,5])

datalee = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//LeeCounty.csv", usecols=[0,5])

datamiamidade = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//MiamiDadeCounty.csv", usecols=[0,5])

dataorange = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//OrangeCounty.csv", usecols=[0,5])

datapalmbeach = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//PalmBeachCounty.csv", usecols=[0,5])

datapinellas = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//PinellasCounty.csv", usecols=[0,5])

datasarasota = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//SarasotaCounty.csv", usecols=[0,5])

dataseminole = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//SeminoleCounty.csv", usecols=[0,5])

datastjohns = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//StJohnsCounty.csv", usecols=[0,5])

datastlucie = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//StLucieCounty.csv", usecols=[0,5])

datavolusia = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//VolusiaCounty.csv", usecols=[0,5])
datamerged = pd.concat([datapalmbeach, datahillsborough, dataseminole, datapinellas, datastjohns, datasarasota, dataescambia, databay, dataorange, datamiamidade, databroward, datavolusia, databrevard, datastlucie, datacollier, datalee, dataduval], axis=0)
df = datamerged
get_ipython().magic('cd C:\\Users\\Robin Junior\\Documents\\My Data Sources\\Noel')
get_ipython().magic('save -f Noel2 1-999999')
datatrade = pd.read_csv("C://Users//Robin Junior//Documents//My Data Sources//IntFlightData.csv")
datatrade['County'] = datatrade['DEST_CITY_NAME'].str.rpartition(',')[0].str.replace(",", " ")
datatrade['State']    = datatrade['DEST_CITY_NAME'].str.rpartition(',')[2]
df[['PASSENGERS','FREIGHT', 'MAIL', 'County', 'State', 'Year']]
datatrade['County'] = datatrade['DEST_CITY_NAME'].str.rpartition(',')[0].str.replace(",", " ")
datatrade['State']    = datatrade['DEST_CITY_NAME'].str.rpartition(',')[2]
df[['PASSENGERS','FREIGHT', 'MAIL', 'County', 'State', 'Year']]
datatrade['County'] = datatrade['DEST_CITY_NAME'].str.rpartition(',')[0].str.replace(",", " ")
datatrade['State']    = datatrade['DEST_CITY_NAME'].str.rpartition(',')[2]
df[['PASSENGERS','FREIGHT', 'MAIL', 'County', 'State', 'Year']]
datatrade['County'] = datatrade['DEST_CITY_NAME'].str.rpartition(',')[0].str.replace(",", " ")
datatrade['State']    = datatrade['DEST_CITY_NAME'].str.rpartition(',')[2]
df[['PASSENGERS','FREIGHT', 'MAIL', 'County', 'State', 'Year']]
datatrade3[['PASSENGERS','FREIGHT', 'MAIL', 'County', 'State', 'Year']]
print(datatrade)
datatrade1 = datatrade[datatrade['State'].str.contains("FL")]
datatrade2 = datatrade1.replace({'West Palm Beach/Palm Beach': 'PalmBeach', 'Tampa': 'Hillsborough', 'Sanford': 'Seminole', 'St. Petersburg': 'Pinellas', 'St. Augustine': 'StJohns', 'Sarasota/Bradenton': 'Sarasota', 'Pensacola': 'Escambia', 'Panama City': 'Bay', 'Fort Lauderdale': 'Broward', 'Daytona Beach': 'Volusia', 'Cocoa Beach': 'Brevard', 'Fort Pierce': 'StLucie', 'Naples': 'Collier','Fort Myers': 'Lee', 'Jacksonville': 'Duval', 'Miami': 'MiamiDade', 'Orlando': 'Orange'}, regex=True)
datatrade3 = datatrade2.groupby('County', as_index=False)['PASSENGERS'].sum()
datatrade4 = datatrade2.groupby('County', as_index=False)['FREIGHT'].sum()
tourtrade = pd.merge(pd.merge(df2,datatrade3,on='County'),datatrade4,on='County')
df2 = df.groupby('County', as_index=False)['Common_Name'].count()
df2=df2.rename(columns = {'Common_Name':'Total_Invasives'})
tourtrade = pd.merge(pd.merge(df2,datatrade3,on='County'),datatrade4,on='County')
print(tourtrade)
get_ipython().magic('save -f Noel2 1-999999')
import Flask
tourtrade.head(1).to_html
tourtrade(1).to_html
tourtrade.head(17).to_html
tourtrade(17).to_html
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import scipy.stats
import seaborn
fig = plt.figure(figsize=(17,5))
fig.add_subplot(121)
seaborn.regplot(x="Total_Invasives", y="PASSENGERS", fit_reg=True, data=tourtrade);
plt.xlabel('Total Invasives 2017');
plt.ylabel('Total Int. Passengers');
plt.title('Tourism vs. Trade');
fig.tight_layout()
plt.show()
fig = plt.figure(figsize=(17,5))
fig.add_subplot(122)
seaborn.regplot(x="Total_Invasives", y="FREIGHT", fit_reg=True, data=tourtrade);
plt.xlabel('Total Invasives 2017');
plt.ylabel('Total Int. Freight');
plt.title('Trade and Plant Invasion');
fig.tight_layout()
plt.show()
fig.add_subplot(121)
seaborn.regplot(x="Total_Invasives", y="PASSENGERS", fit_reg=True, data=tourtrade);
plt.xlabel('Total Invasives 2017');
plt.ylabel('Total Int. Passengers');
plt.title('Tourism and Plant Invasion');

fig.add_subplot(122)
seaborn.regplot(x="Total_Invasives", y="FREIGHT", fit_reg=True, data=tourtrade);
plt.xlabel('Total Invasives 2017');
plt.ylabel('Total Int. Freight');
plt.title('Trade and Plant Invasion');
fig.tight_layout()
plt.show()
print ('Tourism and Plant Invasion')
print (scipy.stats.pearsonr(tourtrade['PASSENGERS'], tourtrade['Total_Invasives']))

print ('Trade and Plant Invasion')
print (scipy.stats.pearsonr(tourtrade['FREIGHT'], tourtrade['Total_Invasives']))
###Pearson r results: Tourism and Plant Invasion (0.698153257112203, 0.0018282275958910359), Trade and Plant Invasion (0.68245302035562039, 0.0025402856333718027). These results show that there is 
###a positive correlation between both the number of passengers and the amount of freight arriving internationally and the amount of non-native plant invasion at the county level in Florida. The p-values for both tourism and trade correlations are less than 1%, indicating that there is a less than 1% chance that this result is random. 
###Calculating the correlation coefficient can determine variability:
###Correlation coefficient for Tourism
0.7**2
###Correlation coefficient for Trade
###More precise correlation coefficient for Tourism
0.698**2
###More precise correlation coefficient for Trade
0.682**2
###Trade can help determine about 48.7% of the variability in plant invasion in Florida counties, while trade can explain approximately 46.5%.
get_ipython().magic('save -f Noel2 1-999999')
