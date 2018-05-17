import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import ast

#reading a csv file
df = pd.read_csv('data.csv')

#filtering data
df_1990 = df.query( 'Year == 1990' )


#we only require infant mortality rate and country
df_infant_country = df_1990[['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)','Country']]
df_infant_country.reset_index(inplace=True)

#splitting and separating average value
df_average = pd.DataFrame(df_infant_country['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split())

#converting string to integer
df_infant_country['average']=df_average.average.apply(ast.literal_eval)

df_infant_country = df_infant_country.sort_values('average')

df10 = df_infant_country.head(10)

plt.pie(df10['average'], labels=df10['Country'])
plt.title("Infant mortality rate by Country")


plt.savefig("Question1_")

plt.show()
