import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import ast


df=pd.read_csv("data.csv")

df1990 = df[ df['Year']==1990 ]
df2 = df1990[['Neonatal mortality rate (per 1000 live births)','Country']]
df2.reset_index(inplace=True)
df2['average'] = pd.DataFrame(df2['Neonatal mortality rate (per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

df1990 = df2.sort_values(['average'])
df_head1990 = df1990.head(5)

plt.bar(df_head1990['Country'],df_head1990['average'])

plt.title("Neonatal mortality rate (per 1000 live births)")
plt.ylabel("mortality rate")
plt.xlabel("Country")

plt.savefig("Question5_")
plt.show()
