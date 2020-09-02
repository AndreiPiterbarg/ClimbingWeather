import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data\Rainier_Weather.csv")




df['Date'] = pd.to_datetime(df['Date'])

# print (df.Date.min())
# print (df.Date.max())
# print(df.head(5))
# print(df.info())


#------------------Plotting Wind Speed Line------------------
# lines = df.plot.line(x="Date", y= "Wind Speed Daily AVG")
# plt.ylabel("")
# plt.xlabel("")
# plt.show()

#------------------Plotting Wind Direction Scatter------------------
# plt.scatter(df.Date, df["Wind Direction AVG"])
# plt.show()

#------------------Plotting Wind Direction Scatter------------------
# ax = sns.heatmap(df.corr(), annot = True, vmin=-1, vmax=1, center= 0, cmap= 'coolwarm')
# plt.show()

df1 = pd.read_csv("Data\climbing_statistics.csv")

df1['Date'] = pd.to_datetime(df1['Date'])

# print(df1.head(5))
# print(df1.info())

# print (df1.Date.min())
# print (df1.Date.max())
df = df.sort_values('Date')
df1 = df1.sort_values('Date')

df2 = pd.merge_asof(df, df1, on='Date')
print(df2.info())

